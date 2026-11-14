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

  void reiniciarMarcador() {
    setState(() {
      contadorLocal = 0;
      contadorVisitante = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: fondo,
      appBar: AppBar(
        backgroundColor: fondo,
        title: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(children: [
            Icon(Icons.sports_basketball_outlined, color: iconogeneral,),
            Text("  Marcador", style: TextStyle(color: textogeneral),)
          ],),
        ),
      ),
      body: Column(
        children: [
          ContadorSuperior(
            contadorLocal: contadorLocal,
            contadorVisitante: contadorVisitante,
          ),
          Spacer(),
          Row(
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
          Spacer(),
          reiniciar(onPressed: reiniciarMarcador)
        ],
      ),
    );
  }
}
