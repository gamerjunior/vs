import 'package:flutter/material.dart';

class ContadorBoton extends StatefulWidget {
  const ContadorBoton({
    super.key,
    required this.color,
    required this.buttonColor,
  });

  final Color color;
  final Color buttonColor;

  @override
  State<ContadorBoton> createState() => _ContadorBotonState();
}

class _ContadorBotonState extends State<ContadorBoton> {
  int contador = 0;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: widget.buttonColor,
            ),
            onPressed: () {
              setState(() {
                contador++;
              });
            },
            child: const Text('+',
              style: TextStyle(
                  color: Color(0xFFFFFFFF)
            )),
          ),
          Container(
            color: widget.color,
            height: 100,
            alignment: Alignment.center,
            child: Text('$contador',
              style: TextStyle(
                  color: Color(0xFFFFFFFF)
            )),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: widget.buttonColor,
            ),
            onPressed: () {
              setState(() {
                contador--;
              });
            },
            child: const Text('-',
              style: TextStyle(
                  color: Color(0xFFFFFFFF)
            )),
          ),
        ],
      ),
    );
  }
}
