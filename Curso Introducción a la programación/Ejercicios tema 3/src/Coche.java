public class Coche  {

    public static void main(String[] args) {
        Puerta miCoche = new Puerta(); // Se crea un objeto
        miCoche.AgregarPuertas();
        System.out.println("El numero de puertas del coche es de: " + miCoche.puertas); //Imprimo el numero de puertas
    }
}
class Puerta {
    public int puertas = 0;  // Numero de puertas inicial

    public void AgregarPuertas() {
        this.puertas++;
    }  // Se le agregan puertas
}
