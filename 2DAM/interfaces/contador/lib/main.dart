import 'package:flutter/material.dart';

void main() {
  runApp(const Contador());
}

class Contador extends StatelessWidget {
  const Contador({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Contador",
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  const Home({super.key});


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: const Text("Contador"),
        leading: Icon(Icons.menu),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Veces pulsado"),
            Center(
              child: Container(
                width: 100,
                height: 100,
                decoration: BoxDecoration(
                  color: Color(0xFF92C5FC),
                  shape: BoxShape.circle
                ),
                child: Text("contador"),
              ),
            )
          ],
        ),
      ),
    );
  }

}
