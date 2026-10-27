package psp.ud2.ejercicio3;

public class Corredor extends Thread {
    String nombre;
    int distancia;
    int randomDelay = (int) (Math.random() * 10);
    boolean finalizado = false;

    public Corredor(String nombre) {
        this.nombre = nombre;
        this.distancia = 0;
    }

    public void esperar() {
        try {
            Thread.sleep(randomDelay);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void run() {
        while( distancia < 1000 && !finalizado){
            distancia++;
            esperar();
        }
        this.finalizado = true;
        System.out.println(nombre + " ha terminado la carrera!");
    }

    public int getdistancia(){

        return this.distancia;
    }
    
}
