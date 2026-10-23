void main() {
  String nombre = 'Portátil';
  double precioUnitario = 899.99;
  int cantidadEnStock = 12;

  final double valorTotalStock = cantidadEnStock * precioUnitario;

  print('Producto: $nombre');
  print('Precio unitario: $precioUnitario €');
  print('Cantidad en stock: $cantidadEnStock');
  print('Valor total del stock: $valorTotalStock €');
}
