import 'package:flutter/material.dart';

import 'screens/home.dart';
import 'themes/theme.dart';

void main() {
  runApp(const Myapp());
}

class Myapp extends StatelessWidget {
  const Myapp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: appTheme,
      title: 'Contador',
      home: const Home(),
    );
  }
}

