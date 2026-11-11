package psp.ud2.ejercicio5;

public class almacen {
    private static final int CAPACIDAD_MAXIMA = 5;
    private int piezasDisponibles;
    private int piezasFabricadas;
    private int piezasEmpaquetadas;

    public almacen() {
        System.out.println("Almacén inicialmente: 0/" + CAPACIDAD_MAXIMA + " piezas.");
    }

    public synchronized void depositarPieza(String trabajador) throws InterruptedException {
        while (piezasDisponibles == CAPACIDAD_MAXIMA) {
            wait();
        }

        piezasDisponibles++;
        piezasFabricadas++;
        System.out.println(trabajador + " deposita una pieza. Almacén: " + piezasDisponibles + "/" + CAPACIDAD_MAXIMA + " piezas.");
        notifyAll();
    }

    public synchronized void retirarPieza(String trabajador) throws InterruptedException {
        while (piezasDisponibles == 0) {
            wait();
        }

        piezasDisponibles--;
        System.out.println(trabajador + " retira una pieza. Almacén: " + piezasDisponibles + "/" + CAPACIDAD_MAXIMA + " piezas.");
        notifyAll();
    }

    public synchronized void registrarEmpaquetado(String trabajador) {
        piezasEmpaquetadas++;
        System.out.println(trabajador + " termina de empaquetar una pieza. Total empaquetadas: "
                + piezasEmpaquetadas + ".");
    }

    public synchronized int getPiezasFabricadas() {
        return piezasFabricadas;
    }

    public synchronized int getPiezasEmpaquetadas() {
        return piezasEmpaquetadas;
    }

    public synchronized int getPiezasDisponibles() {
        return piezasDisponibles;
    }
}
