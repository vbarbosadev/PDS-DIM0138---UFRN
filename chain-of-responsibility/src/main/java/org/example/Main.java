package org.example;

public class Main {

    public static void main(String[] args) {
        Handler bot = new BotHandler();
        Handler n1 = new LevelOneHandler();
        Handler n2 = new LevelTwoHandler();
        Handler gerente = new ManagerHandler();

        bot.setNext(n1).setNext(n2).setNext(gerente);

        Ticket[] tickets = {
            new Ticket(101, "Resetar senha do portal", Severity.LOW),
            new Ticket(102, "Erro intermitente no pagamento", Severity.MEDIUM),
            new Ticket(103, "API fora do ar para um cliente VIP", Severity.HIGH),
            new Ticket(104, "Vazamento de dados suspeito", Severity.CRITICAL)
        };

        System.out.println("=== Chain of Responsibility: Help Desk ===");
        for (Ticket ticket : tickets) {
            System.out.println();
            System.out.printf("Ticket #%d - %s [%s]%n",
                ticket.id(), ticket.description(), ticket.severity());
            bot.handle(ticket);
        }
    }
}
