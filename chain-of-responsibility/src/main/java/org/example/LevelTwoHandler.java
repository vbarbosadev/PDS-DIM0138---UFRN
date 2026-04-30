package org.example;

public class LevelTwoHandler extends AbstractHandler {

    @Override
    protected boolean canHandle(Ticket ticket) {
        return ticket.severity() == Severity.HIGH;
    }

    @Override
    protected void resolve(Ticket ticket) {
        System.out.println("N2 investigou logs e restaurou o servico.");
    }

    @Override
    public String name() {
        return "N2";
    }
}
