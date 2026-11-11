package psp.ud2.ejercicio5;

public class ejecutor {
    public static void main(String[] args) throws InterruptedException {
        almacen almacen = new almacen();

        productor productor1 = new productor("Productor 1", almacen);
        productor productor2 = new productor("Productor 2", almacen);
        consumidor consumidor1 = new consumidor("Consumidor 1", almacen);
        consumidor consumidor2 = new consumidor("Consumidor 2", almacen);

        productor1.start();
        productor2.start();
        consumidor1.start();
        consumidor2.start();

        productor1.join();
        productor2.join();
        consumidor1.join();
        consumidor2.join();

        int fabricadas = almacen.getPiezasFabricadas();
        int empaquetadas = almacen.getPiezasEmpaquetadas();
        int disponibles = almacen.getPiezasDisponibles();

        System.out.println("Proceso finalizado. Fabricadas: " + fabricadas + ", empaquetadas: " + empaquetadas + ", disponibles: " + disponibles + ".");
        if (fabricadas == 20 && empaquetadas == 20 && disponibles == 0) {
            System.out.println("Todas las piezas se han procesado correctamente.");
        } else {
            System.err.println("El proceso no ha terminado correctamente.");
        }
    }
}
