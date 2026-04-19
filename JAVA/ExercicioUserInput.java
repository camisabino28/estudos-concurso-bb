import java.util.Scanner;
import java.util.Locale;

public class ExercicioUserInput {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
//
//        System.out.print("Enter your name: ");
//        String name = scanner.nextLine();
//
//        System.out.print("Enter your age: ");
//        int age = scanner.nextInt();
//
//        System.out.print("What is your gpa: ");
//        double gpa = scanner.nextDouble();
//
//        System.out.print("Are you a student (true/false): ");
//        boolean isStudent = scanner.nextBoolean();
//
//        System.out.println("Hello " + name);
//        System.out.println("You are " + age + " years old");
//        System.out.println("Your gpa is: " + gpa);
//
//        if(isStudent){
//            System.out.println("You are enrolled as a student");
//        }
//        else{
//            System.out.println("You are NOT enrolled");
//        }
//
//        System.out.print("Enter your dog's age: ");
//        int dog_age = scanner.nextInt();
//        scanner.nextLine();  // evita que o proximo input de string considere o enter desse input como input do próximo
//
//        System.out.print("Enter your favorite color: ");
//        String color = scanner.nextLine();
//
//        System.out.println("Your dog is " + dog_age + " years old");
//        System.out.println("You like the color " + color);

        // Exercicio - Calcular area de um retangulo

        double width = 0;
        double height = 0;
        double area = 0;

        System.out.print("Enter the width: ");
        width = scanner.nextDouble();

        System.out.print("Enter the height: ");
        height = scanner.nextDouble();

        area = width * height;

        System.out.println("The area is " + area + " cm²");

        scanner.close();

    }
}
