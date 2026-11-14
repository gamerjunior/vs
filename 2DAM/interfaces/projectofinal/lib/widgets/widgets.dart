import 'package:flutter/material.dart';
import '../themes/theme.dart';

class ContadorBoton extends StatelessWidget {
  const ContadorBoton({
    super.key,
    required this.buttonColor,
    required this.onPressed,
    required this.icono,
  });

  final Color buttonColor;
  final VoidCallback onPressed;
  final Icon icono;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
        minimumSize: Size(MediaQuery.of(context).size.width/5, MediaQuery.of(context).size.height/8), // Tamaño mínimo del botón
        backgroundColor: buttonColor,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15))
      ),
      onPressed: onPressed,
      child: icono
    );
  }
}


class ContadorSuperior extends StatelessWidget {
  final Color colorLocal;
  final Color colorVisitante;
  final int contadorLocal;
  final int contadorVisitante;

  const ContadorSuperior({
    super.key,
    this.colorLocal = local,
    this.colorVisitante = visitante,
    required this.contadorLocal,
    required this.contadorVisitante,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 100,
      padding: const EdgeInsets.symmetric(horizontal: 12),
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          color: extra,
          border: Border.all(color: borde)
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              width: 14,
              height: 14,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: colorLocal,
              ),
            ),
            Text('Local', style: TextStyle(color: colorLocal)),
            Container(
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                color: fondo,
              ),
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    '$contadorLocal',
                    style: TextStyle(color: colorLocal, fontSize: 24),
                  ),
                  const SizedBox(width: 12),
                  Text('VS', style: TextStyle(color: textogeneral)),
                  const SizedBox(width: 12),
                  Text(
                    '$contadorVisitante',
                    style: TextStyle(color: colorVisitante, fontSize: 24),
                  ),
                ],
              ),
            ),
            Text('Visitante', style: TextStyle(color: colorVisitante)),
            Container(
              width: 14,
              height: 14,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: colorVisitante,
              ),
            ),
          ],
        ),
      ),
    );
  }
}


class reiniciar extends StatelessWidget {

  final VoidCallback onPressed;
  final Color color;
  final String text;

  const reiniciar({
    super.key,
    required this.onPressed,
    this.color = extra,
    this.text = 'Reiniciar',
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 200,
      height: 60,
      child: ElevatedButton.icon(
        style: ElevatedButton.styleFrom(
          backgroundColor: color,
          foregroundColor: textogeneral,
          padding: const EdgeInsets.symmetric(horizontal: 16),
          side: BorderSide(color: borde),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15),
          ),
        ),
        onPressed: onPressed,
        icon: const Icon(Icons.refresh),
        label: Text(text),
      ),
    );
  }
}

class Contador extends StatelessWidget{

  final int contador;
  final Color color;
  final Color botoncolor;
  final Color iconoColor;
  final VoidCallback sumar;
  final VoidCallback restar;
  final String equipo;

const Contador({
  super.key,
  required this.contador,
  required this.color,
  required this.botoncolor,
  required this.iconoColor,
  required this.sumar,
  required this.restar,
  required this.equipo,
  });
  @override
  Widget build(BuildContext context){
    return Container(
      alignment: Alignment.center,
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(20),color: color),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ContadorBoton(
            buttonColor: botoncolor,
            onPressed: sumar,
            icono: Icon(Icons.add,
            color: iconoColor,)
          ),
          Container(
            color: color,
            alignment: Alignment.center,
            height: MediaQuery.of(context).size.height/3,
            child: Text(
              '$contador',
              style: const TextStyle(color: textogeneral, fontSize: 100),
            ),
          ),
          ContadorBoton(
            buttonColor: botoncolor,
            onPressed: restar,
            icono: Icon(Icons.remove,
            color: iconoColor)
          ),
          Text("Equipo $equipo",
          style: TextStyle(color: textogeneral))
        ],
      ),
    );
  }
}
 