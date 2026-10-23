import java.io.IOException;
import java.util.Scanner;

//Saúl Sánchez Fernández

public class LanzarProceso {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce la ruta completa al ejecutable: ");
        String ruta = scanner.nextLine();

        try {
            ProcessBuilder pb = new ProcessBuilder(ruta);

            
            Process proceso = pb.start();

            System.out.println("Proceso iniciado correctamente.");
            System.out.println("PID del proceso: " + proceso.pid());

        } catch (IOException e) {
            System.out.println("Error al iniciar el proceso:");
            System.out.println(e.getMessage());

        } catch (SecurityException e) {
            System.out.println("Error de seguridad al iniciar el proceso:");
            System.out.println(e.getMessage());

        } finally {
            scanner.close();
        }
    }
}
