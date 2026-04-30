package org.example;

public abstract class AbstractTicketType implements TicketType {
    private final String category;
    private final String priority;
    private final String sla;

    protected AbstractTicketType(String category, String priority, String sla) {
        this.category = category;
        this.priority = priority;
        this.sla = sla;
    }

    @Override
    public String category() {
        return category;
    }

    @Override
    public String priority() {
        return priority;
    }

    @Override
    public String sla() {
        return sla;
    }

    @Override
    public String summary() {
        return category + " | prioridade " + priority + " | SLA " + sla;
    }
}
