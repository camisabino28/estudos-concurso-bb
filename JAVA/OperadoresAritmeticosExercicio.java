public class OperadoresAritmeticosExercicio {
    public static void main(String[] args){

        // Arithmetics Operators

        int x = 10;
        int y = 3;
        int z;

        //z = x + y;
        //z = x - y;
        //z = x * y;
        //z = x / y;
        //z = x % y;
        //System.out.println(z);

        // Augmented Assignment Operators
        double a = 10;
        double b = 3;

        //a += b;     // isso é igual: a = a + b
        //a -= b;
        //a *= b;
        //a /= b;
        //a %= b;
        //System.out.println(a);

        // Increment and Decrement Operators
        int c = 1;

        //c++;    // isso é igual: c = c + 1
        //c--;
        //System.out.println(c);

        // Order of Operations [P-E-M-D-A-S]

        double result = 3 + 4 * (7 - 5) / 2.0;
        // 3 + 4 * 2 / 2.0  -> parenteses primeiro
        // 3 + 8 / 2.0  -> multiplicação
        // 3 + 4 -> divisão
        // = 7
        System.out.println(result);




    }
}
