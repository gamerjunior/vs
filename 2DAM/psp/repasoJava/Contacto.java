public class Contacto{

    private String nombre;
    private String apellido;
    private int telefono;

    public Contacto(){
        setApellido("vacio");
        setNombre("vacio");
        setTelefono(000000000);
    }

    public Contacto(String nombre, String apellido, int telefono){
        if(nombre != null && !nombre.equals("") && apellido != null && !apellido.equals("") && telefono != 0){
        setApellido(apellido);
        setNombre(nombre);
        setTelefono(telefono);
        }else{
            System.err.println("Los campos no pueden estar vacios");
        }
    
    }


    /*getters y settetrs */
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public String getApellido() {
        return apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    /*sobre escritura de metodos  */
    @Override 
    public String toString(){
        return "nombre: " + this.getNombre() + " apellido: " + this.getApellido() + "telefono: " + this.getTelefono();

    }

    @Override 
    public boolean equals(Object obj){
        if(obj instanceof Contacto){
            Contacto c = (Contacto) obj;
            return this.getTelefono() == c.getTelefono();
        }
        return false;
    }

}

