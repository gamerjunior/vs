package psp.ud2.hilosMultiprocesos;

public class main {
    public static void main(String[] args) {
        HiloContador hilo1 = new HiloContador("Hilo 1");

        Thread thread1 = new Thread(hilo1);

        thread1.start();//primero sale fin del main y despues .start muestra los numero del 1 al diez
        //thread1.run();primero muestra los numero del 1 al 10 y despues  muestra fin del main
        
        System.out.println("fin del main");
        System.exit(0);//detiene la ejecucion del hilo en un numero deferente cada vez
    }
}
