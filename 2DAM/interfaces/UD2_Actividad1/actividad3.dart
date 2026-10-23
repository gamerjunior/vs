void main(){
  double? nota;

  double displayNota = nota?? 0.0;

  String resultado = displayNota >= 5.0 ? "Aprobado" : "Suspenso";

  print("Nota del estudiante: $displayNota | estado final:  $resultado");
  
}