package psp.ud2.ejercicio5.ejercicio5;

import java.util.concurrent.ThreadLocalRandom;

public class consumidor extends Thread {
    private static final int PIEZAS_POR_TRABAJADOR = 10;

    private final almacen almacen;

    public consumidor(String nombre, almacen almacen) {
        super(nombre);
        this.almacen = almacen;
    }

    @Override
    public void run() {
        for (int pieza = 1; pieza <= PIEZAS_POR_TRABAJADOR; pieza++) {
            try {
                almacen.retirarPieza(getName());
                long duracion = ThreadLocalRandom.current().nextLong(1000, 5001);
                System.out.println(getName() + " empaqueta la pieza " + pieza + "/" + PIEZAS_POR_TRABAJADOR + " (" + duracion + " ms).");
                Thread.sleep(duracion);
                almacen.registrarEmpaquetado(getName());
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println(getName() + " ha sido interrumpido.");
                return;
            }
        }
        System.out.println(getName() + " ha terminado de empaquetar.");
    }
}
