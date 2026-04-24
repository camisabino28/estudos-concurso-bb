package POOGG.Aula05;

public class POOAula05GG {
    public static void main(String[] args){
        ContaBanco conta1 = new ContaBanco("Jubileu","CP");
        // Teste das funções
            conta1.info();
            conta1.abrirConta();
            conta1.info();
            conta1.abrirConta();
            conta1.depositar(1000);
            conta1.info();
            conta1.pagarMensal();
            conta1.info();
            conta1.sacar(1200);
            conta1.sacar(1130);
            conta1.info();
            conta1.fecharConta();
            conta1.info();
            conta1.depositar(10);
            conta1.sacar(10);
            conta1.pagarMensal();


        ContaBanco conta2 = new ContaBanco("Creuza","CC");
        // Teste das funções
        conta2.info();
        conta2.abrirConta();
        conta2.info();
        conta2.abrirConta();
        conta2.depositar(1000);
        conta2.info();
        conta2.pagarMensal();
        conta2.info();
        conta2.sacar(1200);
        conta2.sacar(1038);
        conta2.info();
        conta2.fecharConta();
        conta2.info();
        conta2.depositar(10);
        conta2.sacar(10);
        conta2.pagarMensal();
    }
}
