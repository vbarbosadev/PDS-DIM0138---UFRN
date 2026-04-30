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

    enum Severity {
        LOW,
        MEDIUM,
        HIGH,
        CRITICAL
    }

    record Ticket(int id, String description, Severity severity) {
    }

    abstract static class Handler {
        private Handler next;

        public Handler setNext(Handler next) {
            this.next = next;
            return next;
        }

        public final void handle(Ticket ticket) {
            if (canHandle(ticket)) {
                resolve(ticket);
                return;
            }

            if (next == null) {
                System.out.println(name() + " não encontrou próximo atendente.");
                return;
            }

            System.out.println(name() + " encaminhou para " + next.name() + ".");
            next.handle(ticket);
        }

        protected abstract boolean canHandle(Ticket ticket);

        protected abstract void resolve(Ticket ticket);

        protected abstract String name();
    }

    static class BotHandler extends Handler {
        @Override
        protected boolean canHandle(Ticket ticket) {
            return ticket.severity() == Severity.LOW;
        }

        @Override
        protected void resolve(Ticket ticket) {
            System.out.println("Bot resolveu com uma resposta automática.");
        }

        @Override
        protected String name() {
            return "Bot";
        }
    }

    static class LevelOneHandler extends Handler {
        @Override
        protected boolean canHandle(Ticket ticket) {
            return ticket.severity() == Severity.MEDIUM;
        }

        @Override
        protected void resolve(Ticket ticket) {
            System.out.println("N1 resolveu após seguir um procedimento padrão.");
        }

        @Override
        protected String name() {
            return "N1";
        }
    }

    static class LevelTwoHandler extends Handler {
        @Override
        protected boolean canHandle(Ticket ticket) {
            return ticket.severity() == Severity.HIGH;
        }

        @Override
        protected void resolve(Ticket ticket) {
            System.out.println("N2 investigou logs e restaurou o serviço.");
        }

        @Override
        protected String name() {
            return "N2";
        }
    }

    static class ManagerHandler extends Handler {
        @Override
        protected boolean canHandle(Ticket ticket) {
            return ticket.severity() == Severity.CRITICAL;
        }

        @Override
        protected void resolve(Ticket ticket) {
            System.out.println("Gerente assumiu o incidente e acionou o plano de crise.");
        }

        @Override
        protected String name() {
            return "Gerente";
        }
    }
}
