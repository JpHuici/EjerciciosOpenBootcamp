public class Main {

    public static void main(String[] args) {
//3-Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
        //Objeto de la clase Cliente
        Cliente cliente = new Cliente();
        cliente.edad = 27;
        cliente.nombre = "Juan";
        cliente.telefono = 123456789;
        cliente.credito = 120;

        System.out.println("Cliente: ");
        System.out.println(cliente.nombre);
        System.out.println(cliente.edad);
        System.out.println(cliente.telefono);
        System.out.println(cliente.credito);
//4-Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
        //Objeto de la clase Trabajador
        Trabajador trabajador = new Trabajador();
        trabajador.edad = 37;
        trabajador.nombre = "Pedro";
        trabajador.telefono = 12345987;
        trabajador.salario = 1600;

        System.out.println("Trabajador: ");
        System.out.println(trabajador.nombre);
        System.out.println(trabajador.edad);
        System.out.println(trabajador.telefono);
        System.out.println(trabajador.salario);
    }
}
//1-Crea una clase Persona con las siguientes variables: La edad, El nombre, El teléfono.
class Persona {
        int edad;
        String nombre;
        int telefono;
}
//2-Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
class Cliente extends Persona {
        int credito;
}
class Trabajador extends Persona {
        int salario;
}
