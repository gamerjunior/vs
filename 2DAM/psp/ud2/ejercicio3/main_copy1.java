package psp.ud2.ejercicio3;

public class main_copy1 {
    
    public static void main(String[] args) {
        
        Corredor A = new Corredor("A");
        Corredor B = new Corredor("B");
        Corredor C = new Corredor("C");

        A.start();
        B.start();
        C.start();

        while (true) { 
            if(A.getdistancia() >= 1000 || B.getdistancia() >= 1000 || C.getdistancia() >= 1000){
                A.esperar();
                B.esperar();
                C.esperar();
                break;
            }
            
            System.out.println("A: " + A.getdistancia() + " B: " + B.getdistancia() + " C: " + C.getdistancia());

            try {
                Thread.sleep(100);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


}
