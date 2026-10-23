void main() {
  String nombre_empleado = "Juan Pérez";
  int horas_trabajadas = 40;
  int nota_desempenio = 8;
  bool faltas_injustificadas = false;


  if(horas_trabajadas >= 40 && nota_desempenio >= 8 && !faltas_injustificadas) {
    print("evaluación de bono para $nombre_empleado: apto para recibir el bono de productividad");
  } else {
    print("El empleado $nombre_empleado no es elegible para un bono.");
  }
}
