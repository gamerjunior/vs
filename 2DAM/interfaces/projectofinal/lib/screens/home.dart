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
      if(contadorLocal > 0){
        contadorLocal--;
      }
      
    });
  }

  void sumarVisitante() {
    setState(() {
      contadorVisitante++;
    });
  }

  void restarVisitante() {
    setState(() {
      if(contadorVisitante > 0){
        contadorVisitante--;
      }
    });
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
