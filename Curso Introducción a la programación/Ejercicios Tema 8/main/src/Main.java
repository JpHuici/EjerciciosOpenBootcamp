public class Main {

    //Crear clase Persona.
    //Crear variables las privadas edad, nombre y telefono de la clase Persona.

    static class Persona {
        private int edad;
        private String nombre;
        private int telefono;

        //Crear gets y sets de cada propiedad.

        //SETTERS
        public void setEdad(int edad) {
            this.edad = 27;
        }
        public void setNombre(String nombre) {
            this.nombre = "Juan";
        }
        public void setTelefono(int telefono) {
            this.telefono = 123456789;
        }

        //GETTERS
        public int getEdad() {
            return  this.edad;
        }
        public String getNombre() {
            return  this.nombre;
        }
        public int getTelefono() {
            return  this.telefono;
        }

    }

    //Crear un objeto persona en el main.
    //Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setEdad(27);
        persona.setTelefono(123456789);
        persona.setNombre("Juan");

        System.out.println(persona.getNombre());
        System.out.println(persona.getEdad());
        System.out.println(persona.getTelefono());

    }

}
