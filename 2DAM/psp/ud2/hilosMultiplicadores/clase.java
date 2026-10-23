package psp.ud2.hilosMultiplicadores;

public class clase extends Thread {
    private int numero;

    public clase(int numero) {
        this.numero = numero;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));
        }
    }

    public static void main(String[] args) {
       for (int numero = 1; numero <= 10; numero++) {
            clase hilo = new clase(numero);
            hilo.start();
            try {
                hilo.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                return;
            }
        }
    }
        

    //no se muestran las tabls en orden
    //si, se intercalan las distintas llineas
    //por que cada hilo se ejecuta de manera independiente y el planificador de hilos decide en qué orden se ejecutan
}


