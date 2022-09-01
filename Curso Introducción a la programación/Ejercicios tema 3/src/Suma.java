import java.util.Scanner;

public class Suma {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        int numero1,numero2,numero3,resultado;
        System.out.print("Ingrese el primer numero: ");
        //Ingreso los 3 valores
        numero1 = num.nextInt();
        System.out.print("Ingrese el segundo numero: ");
        numero2 = num.nextInt();
        System.out.print("Ingrese el tercer numero: ");
        numero3 = num.nextInt();

        resultado = numero1 + numero2 + numero3; //Calculo la suma de los 3 números

        System.out.println("El resultado de la suma es: " + resultado); //Imprimo el resultado de la suma
        }
    }
