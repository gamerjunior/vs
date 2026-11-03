package psp.ud2;

public class ejercicio4_ssf {
    
    private static int entradas = 100;

    public static synchronized boolean venderEntrada(String vendedor) {

        if (entradas > 0) {
            entradas--;

            System.out.println(vendedor + " ha vendido una entrada "+ "quedan " + entradas + " entradas");

            return true;
        }

        return false;
    }

    public static void main(String[] args) {

        
        Thread vendedor1 = new Thread(new Vendedor("Vendedor 1"));
        Thread vendedor2 = new Thread(new Vendedor("Vendedor 2"));
        Thread vendedor3 = new Thread(new Vendedor("Vendedor 3"));
        
        vendedor1.start();
        vendedor2.start();
        vendedor3.start();

        try {
            vendedor1.join();
            vendedor2.join();
            vendedor3.join();

        } catch (InterruptedException e) {
            System.out.println("Se ha interrumpido la espera.");
            Thread.currentThread().interrupt();
        }

        System.out.println("VENTA FINALIZADA");
        System.out.println("Entradas restantes: " + entradas);
    }
}

class Vendedor implements Runnable {

    private String nombre;

    public Vendedor(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public void run() {

        while (true) {

            try {
                int tiempo = (int) (Math.random() * 91) + 10;

                Thread.sleep(tiempo);

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }

            boolean vendida = ejercicio4_ssf.venderEntrada(nombre);

            if (!vendida) {
                System.out.println(nombre + ": No quedan entradas.");
                break;
            }
        }

        System.out.println(nombre + " ha terminado de vender.");
    }
}
