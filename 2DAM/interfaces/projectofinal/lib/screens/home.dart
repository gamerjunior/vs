import 'package:flutter/material.dart';

import '../themes/theme.dart';
import '../widgets/widgets.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int contadorLocal = 0;
  int contadorVisitante = 0;

  void sumarLocal() {
    setState(() {
      contadorLocal++;
    });
  }

  void restarLocal() {
    setState(() {
      contadorLocal--;
    });
  }

  void sumarVisitante() {
    setState(() {
      contadorVisitante++;
    });
  }

  void restarVisitante() {
    setState(() {
      contadorVisitante--;
    });
  }

  Widget Contador({
    required int contador,
    required Color color,
    required Color botoncolor,
    required Color iconoColor,
    required VoidCallback sumar,
    required VoidCallback restar,
    required String equipo,
  }) {
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
          Text("Equipo " + equipo,
          style: TextStyle(color: textogeneral))
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Contador'),
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Contador(
            contador: contadorLocal,
            color: local,
            botoncolor: localBoton,
            iconoColor: iconogeneral,
            sumar: sumarLocal,
            restar: restarLocal,
            equipo: "local"
          ),
          Contador(
            contador: contadorVisitante,
            color: visitante,
            botoncolor: visitanteBoton,
            iconoColor: iconogeneral,
            sumar: sumarVisitante,
            restar: restarVisitante,
            equipo: "Visitante"
          ),
        ],
      ),
    );
  }
}
