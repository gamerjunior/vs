double multiplicacion(double a, int b, {int? c}) {
  if (c != null) {
    return a * b * c;
  }
  return a * b;
}

double operacion(double a, int b, {required String operacion}) {
  if (operacion == 'multiplicacion') {
    return a * b;
  }else if (operacion == 'suma') {
    return a + b;
  } else if (operacion == 'resta') {
    return a - b;
  } else if (operacion == 'division') {
    return a / b;
  }
  return 0.0;
}

double division(double a, int b) {
  try {
    a/b;
  } catch (e) {
    print('Error: ${e.toString()}');
  }finally {
    print('Operación finalizada');
  }
  return a / b;
}


void main() {
  print(operacion(10.0, 5, operacion: 'multiplicacion'));
  print(operacion(10.0, 5, operacion: 'suma'));
  print(operacion(10.0, 5, operacion: 'resta'));
  print(operacion(10.0, 5, operacion: 'division'));
}