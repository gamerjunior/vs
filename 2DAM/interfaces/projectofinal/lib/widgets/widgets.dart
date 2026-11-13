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
        minimumSize: const Size(150, 150),
        backgroundColor: buttonColor,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15))
      ),
      onPressed: onPressed,
      child: icono
    );
  }
}


class ContadorSuperior extends StatelessWidget{
  final Color color;
  final Color colorLocal;
  final Color colorVisitante;
  
  const ContadorSuperior({
    super.key,
    this.color = extra,
    this.colorLocal = local,
    this.colorVisitante = visitante
  });
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Container(
      width: 200,
      height: 100,
      child: Row(
        children: [
          Container(
            decoration: BoxDecoration( shape: BoxShape.circle,
             color: colorLocal),
          ),
          Text
      ],
      )
    );
  }

}


class reiniciar extends StatelessWidget {
  const reiniciar({
    super.key,
    required this.onPressed,
    this.color = extra,
    this.text = 'Reiniciar',
  });

  final VoidCallback onPressed;
  final Color color;
  final String text;

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
            height: MediaQuery.of(context).size.height/2,
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
 