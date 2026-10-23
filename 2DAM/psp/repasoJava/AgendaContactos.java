
import java.util.ArrayList;
import java.util.Scanner;

public class AgendaContactos {
    static Scanner teclado = new Scanner(System.in);
    static ArrayList<Contacto> contactos = new ArrayList<>();
    public static void main(String[] args) {
        menu();
        
    }

    public static void menu(){
        int num = 0;
        while(num > 5 ||  num < 1){
            System.out.println("Elige una opción");
            System.out.println("1. añadir contacto");
            System.out.println("2. buscar contacto");
            System.out.println("3. modificar un contacto");
            System.out.println("4. eliminar un contacto");
            System.out.println("5. salir");
            System.out.println("Respuesta: ");
            if(teclado.hasNextInt()){
                num=teclado.nextInt();
            }else{
                System.err.println("Introduce un valor valido");
                teclado.next();
            }
            switch(num){
                case 1:
                    AnadirContacto();
                    break;
                case 2:
                    BuscarContactos();
                    break;
                case 3:
                    ModificarContacto();
                    break;
                case 4:
                    EliminarContacto();
                    break;
                case 5:
                    System.out.println("Saliendo del programa");
                    break;
                default:
                    System.err.println("Introduce un valor valido");
            }
        }

        teclado.close();
    }

    public static void AnadirContacto(){
        Contacto nuevo = new Contacto();
        System.out.println("Nombre del contacto: ");
        String nombre = teclado.nextLine();
        System.out.println("Apellido del contacto: ");
        String apellido = teclado.nextLine();
        System.out.println("Telefono:");
        int telefono = teclado.nextInt();

        nuevo.setApellido(apellido);
        nuevo.setNombre(nombre); 
        nuevo.setTelefono(telefono);

        contactos.add(nuevo);
    }

    public static void BuscarContactos(){
        System.out.println("Introduce el numero o nombre del contacto a buscar: ");
        String busqueda = teclado.nextLine();
        for(Contacto c : contactos){
            if(c.getTelefono() == Integer.parseInt(busqueda) || c.getNombre().equals(busqueda) ){
                System.out.println(c);
                break;
            }
        }
    }

    public static void ModificarContacto(){
        System.out.println("Introduce el numero o nombre del contacto a modificar: ");
        String busqueda = teclado.nextLine();
        for(Contacto c : contactos){
            if(c.getTelefono() == Integer.parseInt(busqueda) || c.getNombre().equals(busqueda) ){
                System.out.println("Introduce el nuevo nombre: ");
                String nombre = teclado.nextLine();
                System.out.println("Introduce el nuevo apellido: ");
                String apellido = teclado.nextLine();
                System.out.println("Introduce el nuevo telefono: ");
                int telefono = teclado.nextInt();

                c.setApellido(apellido);
                c.setNombre(nombre); 
                c.setTelefono(telefono);
                break;
            }
        }
    }

    public static void EliminarContacto(){
        System.out.println("Introduce el numero o nombre del contacto a eliminar: ");
        String busqueda = teclado.nextLine();
        for(Contacto c : contactos){
            if(c.getTelefono() == Integer.parseInt(busqueda) || c.getNombre().equals(busqueda) ){
                contactos.remove(c);
                break;
            }
        }
    }

}
