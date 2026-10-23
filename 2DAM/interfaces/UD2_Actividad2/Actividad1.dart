
double calcularPrecioTotal(double precioUnitario, int cantidad) {
  return precioUnitario * cantidad;
}

String generarEtiqueta(String nombre, String codigo) {
  return "[$codigo]-$nombre";
}

bool verificarStock(int stockDisponible, int stockRequerido) {
  return stockDisponible >= stockRequerido;
}

void main() {
  double total = calcularPrecioTotal(450.50, 3);
  print("Precio total: \$$total");

  String etiqueta = generarEtiqueta('Laptop Gamer', 'ART-9988');
  print(etiqueta);

  bool hayStock = verificarStock(5, 10);
  print("¿Hay suficiente stock?: $hayStock");
}