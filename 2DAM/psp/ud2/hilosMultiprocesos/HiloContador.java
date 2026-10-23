package psp.ud2.hilosMultiprocesos;

public class HiloContador implements Runnable {
    private int contador;
    private String nombre;

    public HiloContador(String nombre) {
        this.contador = 0;
        this.nombre = nombre;
    }

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            contador++;
            System.out.println(nombre + " - Contador: " + contador);
        }
    }
    
}
