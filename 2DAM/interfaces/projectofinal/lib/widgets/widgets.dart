import 'package:flutter/material.dart';

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
