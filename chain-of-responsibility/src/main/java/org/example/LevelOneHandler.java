package org.example;

public class LevelOneHandler extends AbstractHandler {

    @Override
    protected boolean canHandle(Ticket ticket) {
        return ticket.severity() == Severity.MEDIUM;
    }

    @Override
    protected void resolve(Ticket ticket) {
        System.out.println("N1 resolveu apos seguir um procedimento padrao.");
    }

    @Override
    public String name() {
        return "N1";
    }
}
