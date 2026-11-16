import 'package:flutter/material.dart';

import '../themes/theme.dart';
import '../widgets/widgets.dart';

// Pantalla principal del marcador deportivo.
// Es un StatefulWidget porque su contenido cambia en tiempo real
// cuando se suma o resta puntos a cada equipo.
class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

// Clase de estado que guarda los valores actuales del marcador.
class _HomeState extends State<Home> {
  // Contador del equipo local.
  int contadorLocal = 0;

  // Contador del equipo visitante.
  int contadorVisitante = 0;

  // Suma un punto al equipo local y vuelve a construir la pantalla.
  void sumarLocal() {
    setState(() {
      contadorLocal++;
    });
  }

  // Resta un punto al equipo local, pero nunca permite que baje de 0.
  void restarLocal() {
    setState(() {
      if (contadorLocal > 0) {
        contadorLocal--;
      }
    });
  }

  // Suma un punto al equipo visitante y actualiza la interfaz.
  void sumarVisitante() {
    setState(() {
      contadorVisitante++;
    });
  }

  // Resta un punto al equipo visitante, pero no permite valores negativos.
  void restarVisitante() {
    setState(() {
      if (contadorVisitante > 0) {
        contadorVisitante--;
      }
    });
  }

  // Reinicia el marcador de ambos equipos a cero.
  void reiniciarMarcador() {
    setState(() {
      contadorLocal = 0;
      contadorVisitante = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Fondo general de la pantalla.
      backgroundColor: fondo,

      // Barra superior con el título del marcador.
      appBar: AppBar(
        backgroundColor: fondo,
        title: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            children: [
              // Icono de deporte para identificar la pantalla.
              Icon(
                Icons.sports_basketball_outlined,
                color: iconogeneral,
              ),
              // Título visible en la app bar.
              Text(
                "  Marcador",
                style: TextStyle(color: textogeneral),
              )
            ],
          ),
        ),
      ),

      // Cuerpo principal: se organiza en columnas para mostrar
      // el marcador superior, los dos contadores y el botón de reinicio.
      body: Column(
        children: [
          // Muestra el marcador global con el resultado actual.
          ContadorSuperior(
            contadorLocal: contadorLocal,
            contadorVisitante: contadorVisitante,
          ),

          // Espaciado flexible para centrar los contadores verticalmente.
          Spacer(),

          // Fila con los dos paneles de equipos.
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              // Contador del equipo local.
              Contador(
                contador: contadorLocal,
                color: local,
                botoncolor: localBoton,
                iconoColor: iconogeneral,
                sumar: sumarLocal,
                restar: restarLocal,
                equipo: "local",
              ),

              // Contador del equipo visitante.
              Contador(
                contador: contadorVisitante,
                color: visitante,
                botoncolor: visitanteBoton,
                iconoColor: iconogeneral,
                sumar: sumarVisitante,
                restar: restarVisitante,
                equipo: "Visitante",
              ),
            ],
          ),

          // Otro espacio para separar el botón de reinicio.
          Spacer(),

          // Botón que llama a la función de reinicio del marcador.
          reiniciar(onPressed: reiniciarMarcador),
        ],
      ),
    );
  }
}
