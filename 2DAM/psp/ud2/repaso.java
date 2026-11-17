package psp.ud2;


public class repaso {
    class urna{
        int candidato1;
        int candidato2;
        int candidato3;


        public urna(){
            this.candidato1 = 0;
            this.candidato2 = 0;
            this.candidato3 = 0;
        }

        public synchronized void votar(){
            int voto =  (int)(Math.random() * 3) + 1;
            switch (voto) {
                case 1:
                    candidato1++;
                    break;
                case 2:
                    candidato2++;
                    break;
                case 3:
                    candidato3++;
                    break;
                default:
                    break;
            }
        }

        public void votos(){
            System.out.println("candidato 1: " + candidato1);
            System.out.println("candidato 2: " + candidato2);
            System.out.println("candidato 3: " + candidato3);
        }

    }


    class votante extends Thread{
        private urna urna;
        votante(urna u){
            this.urna = u;
        }

        @Override 
        public void run(){
            urna.votar();
        }
    }


    public static void main(String[] args) throws InterruptedException{
        repaso r = new repaso();
        urna u = r.new urna();

       votante[] votantes = new votante[100];

        for (int i = 0; i < votantes.length; i++) {
            votantes[i] = r.new votante(u);
            votantes[i].start();
        }

        for (votante v : votantes) {
            v.join();
        }

        u.votos();

    }

    

}
