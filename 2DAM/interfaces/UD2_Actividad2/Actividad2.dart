String crearPerfil(String nombre, [int? edad, String? ciudad]) {
  String perfil = "Nombre: $nombre";
  if (edad != null) {
    perfil += ", Edad: $edad";
  }
  if (ciudad != null) {
    perfil += ", Ciudad: $ciudad";
  }
  return perfil;
}

enviarNotificacion(String mensaje, {String? remitente = "Sistema", int? prioridad}) {
  String notificacion = "Mensaje: $mensaje";
  if (remitente != null) {
    notificacion += ", Remitente: $remitente";
  }
  if (prioridad != null) {
    notificacion += ", Prioridad: $prioridad";
  }
  print(notificacion);
}

actualizarPassword(String usuario, {required String nuevaPassword, required String confirmarPassword, required String tokenSeguridad}){
  if (nuevaPassword == confirmarPassword) {
    return "Contraseña actualizada exitosamente para el usuario $usuario.";
  } else {
    return "Error: Las contraseñas no coinciden. No se pudo actualizar la contraseña para el usuario $usuario.";
  }
}


void main() {
  // 1. Prueba de parámetros opcionales posicionales
  print(crearPerfil('Carlos'));
  print(crearPerfil('Ana', 28, 'Madrid'));

  print(''); // Línea en blanco para separar

  // 2. Prueba de parámetros con nombre opcionales
  enviarNotificacion('Tu sesión está por expirar');
  enviarNotificacion('Actualización disponible', remitente: 'Admin', prioridad: 3);

  // 3. Prueba de parámetros con nombre OBLIGATORIOS (required)
  String resultadoExitoso = actualizarPassword(
    'carlos123',
    nuevaPassword: 'miPasswordSegura123',
    confirmarPassword: 'miPasswordSegura123',
    tokenSeguridad: 'TOKEN-ABC-123',
  );
  print(resultadoExitoso);

  String resultadoError = actualizarPassword(
    'ana_dev',
    nuevaPassword: '12345Password',
    confirmarPassword: 'PasswordDiferente',
    tokenSeguridad: 'TOKEN-XYZ-789',
  );
  print(resultadoError);
}