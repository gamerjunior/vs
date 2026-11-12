import 'package:flutter/material.dart';

import '../themes/theme.dart';
import '../widgets/widgets.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text('Contador'),
      ),
      body: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          ContadorBoton(
            color: local,
            buttonColor: localBoton,
          ),
          ContadorBoton(
            color: visitante,
            buttonColor: visitanteBoton,
          ),
        ],
      ),
    );
  }
}
