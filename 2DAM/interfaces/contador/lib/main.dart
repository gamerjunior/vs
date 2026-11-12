import 'package:flutter/material.dart';

import 'screens/home.dart';
import 'themes/theme.dart';

void main() {
  runApp(const Contador());
}

class Contador extends StatelessWidget {
  const Contador({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: appTheme,
      title: 'Contador',
      home: const Home(),
    );
  }
}

