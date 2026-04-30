package org.example;

public class BotHandler extends AbstractHandler {

    @Override
    protected boolean canHandle(Ticket ticket) {
        return ticket.severity() == Severity.LOW;
    }

    @Override
    protected void resolve(Ticket ticket) {
        System.out.println("Bot resolveu com uma resposta automatica.");
    }

    @Override
    public String name() {
        return "Bot";
    }
}
