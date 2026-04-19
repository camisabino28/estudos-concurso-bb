public class PrimeiroPrograma {
    public static void main(String[] args) {
        // System.out.println("Hello, World!");
        // ✅ variável = um recipiente reutilizável para um valor
        //             a variável se comporta como se fosse o próprio valor que ela contém

        // 🟥 Primitivo = valor simples armazenado diretamente na memória (stack)
        // 🟦 Referência = endereço de memória (stack) que aponta para o objeto real (heap)

        // 🟥 Primitivo   vs   🟦 Referência
        // ----------          ----------
        // int                 String
        // double              array
        // char                object
        // boolean

        // 2 Passos para criar uma variável:
        // ----------------------------------
        // 1. declaração
        // 2. atribuição

        int age = 22;
        //  System.out.println(age);

        int year = 2026;
        // System.out.println("O ano é " + year);

        double price = 3.99;
        double gpa = 3.5;
        double temperature = -12.5;
        // System.out.println("$" + price);

        char grade = 'A';
        char symbol = '!';
        char currency = '$';
        // System.out.println(grade);

        boolean isStudent = true;
        boolean forSale = false;
        boolean isOnline = true;
        // System.out.println(isStudent);

        String name = "Camila";
        String food = "Pizza";
        String email = "fake123@gmail.com";
        String car = "Mustang";
        String color = "red";
        // System.out.println("Hello " + name);

        // Exercicios
        System.out.println("You are " + age + " years old");
        System.out.println("Your gpa is: " + gpa);
        System.out.println("Your average letter grade is: " + grade);

        System.out.println("Your choice is a " + color + " " + year + " " + car );
        System.out.println("The price is: " + currency + price);

        if(forSale){
            System.out.println("There is a " + car + " for sale");
        }
        else{
            System.out.println("The " + car + " is not for sale");
        }
    }
}
