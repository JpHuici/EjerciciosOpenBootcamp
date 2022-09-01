//Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
class SentenciaIf {
    public static void main(String[] args) {
        int numeroIf = 0;
        if (numeroIf < 0) {
            System.out.println("El numero es negativo.");//Si la variable es menor a cero, el número es negativo.
        } else if (numeroIf > 0) {
            System.out.println("El número es positivo.");//Si la variable es mayor a cero,el número es positivo.
        } else {
            System.out.println("El número es cero.");//La única condición restante, es que el número sea cero.
        }

    }
}



//Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
//Incrementar el valor de la variable en uno cada vez que se ejecute.
// Mostrarlo por pantalla cada vez que se ejecute.
class BucleWhile {
        public static void main(String[] args) {
            int numeroWhile = 0;
            while (numeroWhile < 3) {
                System.out.println(numeroWhile);//El bucle comienza en cero y terminará en dos, por lo que se imprime 0,1,2.
                numeroWhile++;
            }
        }
    }


//Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
class BucleDoWhile {
    public static void main(String[] args) {
        int numeroDoWhile = 0;
        do {
            System.out.println(numeroDoWhile);//El bucle llega a ejecutarse sólo una vez ya que cuando verifica la condición, esta no se cumple.
            numeroDoWhile ++;
        } while (numeroDoWhile < 0);
    }
}
//Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
class BucleFor {
    public static void main(String[] args) {
        for(int numeroFor = 0; numeroFor <= 3; numeroFor++)
            System.out.println(numeroFor);//El bucle llega a ejecutarse 4 veces, se imprime 0,1,2,3.
    }
}
//Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
class SentenciaSwitch {
    public static void main(String[] args) {
        var estacion = "verano";//Si la variable estacion se modifica, el mensaje cambia.
        switch(estacion) {
            case "invierno":
                System.out.println("Abrigate! Estamos en invierno.");
                break;
            case "primavera":
                System.out.println("Las plantas florecen! Estamos en primavera.");
                break;
            case "verano":
                System.out.println("A cuidarse del sol! Estamos en Verano.");
                break;
            case "otoño":
                System.out.println("Las hojas caen, Estamos en otoño.");
                break;
            default:
                System.out.println("Prueba de nuevo, el caracter ingresado no es una estación");//En caso de que ingrese una variable no especificada,se imprime el mensaje default.
        }
    }
}
