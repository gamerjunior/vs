"""Comprobador del simulacro (alumno). Uso: python comprobar_simulacro.py ruta/programa.py [carpeta_datos]"""
import csv, json, os, shutil, subprocess, sys, tempfile
import xml.etree.ElementTree as ET

EXP = {'json': {'fichajes_validos': 3, 'empleados': [{'id': 'E01', 'nombre': 'Lucía Pons', 'departamento': 'Taller', 'horas': 8.5, 'importe': 85.0}, {'id': 'E02', 'nombre': 'Raúl Mir', 'departamento': 'Oficina', 'horas': 8.0, 'importe': 120.0}, {'id': 'E03', 'nombre': 'Nuria Vila', 'departamento': 'Taller', 'horas': 0.0, 'importe': 0.0}]}, 'err': [['linea', 'motivo', 'contenido'], ['4', 'empleado desconocido', 'E07;2026-10-05;09:00;10:00'], ['5', 'salida no posterior a entrada', 'E01;2026-10-06;10:00;09:00'], ['6', 'hora invalida', 'E02;2026-10-06;09:00;']], 'xml': [{'nombre': 'Oficina', 'empleados': '1', 'horas': '8.00', 'importe': '120.00'}, {'nombre': 'Taller', 'empleados': '2', 'horas': '8.50', 'importe': '85.00'}]}
PROG = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "nomina.py")
DATOS = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "ejemplo")
T = tempfile.mkdtemp()
for n in ("empleados.json", "fichajes.csv"):
    shutil.copy(os.path.join(DATOS, n), T)
shutil.copy(PROG, os.path.join(T, "programa.py"))
try:
    r = subprocess.run([sys.executable, "programa.py"], cwd=T, capture_output=True, text=True, timeout=30)
except subprocess.TimeoutExpired:
    r = None


def p(n):
    return os.path.join(T, n)


def ejecuta():
    assert r is not None and r.returncode == 0, (r.stderr.strip().splitlines() or ["error"])[-1] if r else "timeout"
    for n in ("horas.json", "errores.csv", "departamentos.xml"):
        assert os.path.exists(p(n)), f"no se ha generado {n}"


def j_estructura():
    d = json.load(open(p("horas.json"), encoding="utf-8"))
    assert d["fichajes_validos"] == EXP["json"]["fichajes_validos"], f"fichajes_validos {d['fichajes_validos']}"
    assert [e["id"] for e in d["empleados"]] == [e["id"] for e in EXP["json"]["empleados"]], "empleados/orden"


def j_valores():
    d = json.load(open(p("horas.json"), encoding="utf-8"))["empleados"]
    for e, x in zip(d, EXP["json"]["empleados"]):
        assert set(e) == set(x), f"claves {sorted(e)}"
        assert e["nombre"] == x["nombre"] and e["departamento"] == x["departamento"], e["id"]
        assert abs(e["horas"] - x["horas"]) < 0.006, f"{e['id']}: horas {e['horas']}, esperado {x['horas']}"
        assert abs(e["importe"] - x["importe"]) < 0.006, f"{e['id']}: importe {e['importe']}, esperado {x['importe']}"
    t = open(p("horas.json"), encoding="utf-8").read()
    assert "\\u" not in t and "\n  " in t, "acentos escapados o sin indent"


def e_lineas():
    filas = list(csv.reader(open(p("errores.csv"), encoding="utf-8", newline="")))
    assert filas[0] == ["linea", "motivo", "contenido"], "cabecera"
    assert [f[0] for f in filas[1:]] == [f[0] for f in EXP["err"][1:]], f"líneas {[f[0] for f in filas[1:]]}"


def e_contenido():
    filas = list(csv.reader(open(p("errores.csv"), encoding="utf-8", newline="")))[1:]
    for f, x in zip(filas, EXP["err"][1:]):
        assert f[1].strip(), f"línea {f[0]}: motivo vacío"
        assert f[2] == x[2], f"línea {f[0]}: contenido {f[2]!r}, esperado {x[2]!r}"


def x_deps():
    r_ = ET.parse(p("departamentos.xml")).getroot()
    assert r_.tag == "departamentos"
    got = [d.get("nombre") for d in r_]
    assert got == [x["nombre"] for x in EXP["xml"]], f"departamentos {got} (orden alfabético)"


def x_valores():
    for d, x in zip(ET.parse(p("departamentos.xml")).getroot(), EXP["xml"]):
        for k in ("empleados", "horas", "importe"):
            assert d.get(k) is not None and abs(float(d.get(k)) - float(x[k])) < 0.006, f"{x['nombre']}: {k}={d.get(k)}, esperado {x[k]}"


CHECKS = [("el programa se ejecuta y genera 3 ficheros", ejecuta, 1.0),
          ("horas.json: estructura y orden", j_estructura, 1.5),
          ("horas.json: horas, importes y formato", j_valores, 2.0),
          ("errores.csv: líneas rechazadas", e_lineas, 1.5),
          ("errores.csv: motivo y contenido original", e_contenido, 1.0),
          ("departamentos.xml: departamentos y orden", x_deps, 0.75),
          ("departamentos.xml: empleados, horas, importe", x_valores, 0.75)]
tot = 0.0
for nom, fn, pts in CHECKS:
    try:
        fn(); tot += pts; print(f"  OK     {nom:50} +{pts}")
    except Exception as e:
        print(f"  FALLA  {nom:50} 0/{pts} -> {type(e).__name__}: {e}")
print(f"\nPuntos automáticos: {tot:.2f} / 8.50   (+1.5 por RNF y calidad, a valorar a mano)")
