package org.example;

public class ManagerHandler extends AbstractHandler {

    @Override
    protected boolean canHandle(Ticket ticket) {
        return ticket.severity() == Severity.CRITICAL;
    }

    @Override
    protected void resolve(Ticket ticket) {
        System.out.println("Gerente assumiu o incidente e acionou o plano de crise.");
    }

    @Override
    public String name() {
        return "Gerente";
    }
}
