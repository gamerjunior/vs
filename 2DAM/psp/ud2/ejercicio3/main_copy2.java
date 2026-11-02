package psp.ud2.ejercicio3;

public class main_copy2 {
    
    public static void main(String[] args) {
        
        Corredor A = new Corredor("A");
        Corredor B = new Corredor("B");
        Corredor C = new Corredor("C");

        A.start();
        B.start();
        C.start();

        while (true) { 
            if(B.getdistancia() >= 1000 || C.getdistancia() >= 1000){
                B.esperar();
                C.esperar();
                break;
            }
            if(A.getdistancia() >= 700 ){
                
                A.interrupt();
            }
            if(A.isInterrupted()){
                System.out.println("A: terminated" + " B: " + B.getdistancia() + " C: " + C.getdistancia());
            }else{
                System.out.println("A: " + A.getdistancia() + " B: " + B.getdistancia() + " C: " + C.getdistancia());
            }

            try {
                Thread.sleep(100);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


}
