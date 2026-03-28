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

        int age = 21;
        System.out.println(age);

        int year = 2026;
        System.out.println("O ano é " + year);

        double price = 3.99;
        double gpa = 3.5;
        double temperature = -12.5;
        System.out.println("$" + price);
    }
}
