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
              style: const TextStyle(color: textogeneral),
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
 