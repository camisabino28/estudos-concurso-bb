import java.util.Random;

public class RandomNumbers {
    public static void main(String[] args){

        Random random = new Random();

        double number1;
        int number2;
        boolean isHeads;


        number1 = random.nextDouble();  // segundo argumento é exclusivo então tem que acrescentar +1
        number2 = random.nextInt(1,101);
        isHeads = random.nextBoolean();

        System.out.println(number1);
        System.out.println(number2);
        if(isHeads){
            System.out.println("HEADS");
        }
        else{
            System.out.println("TAILS");
        }
    }
}
