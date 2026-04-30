package org.example;

public interface TicketTypeFactory {

    TicketType get(String category, String priority, String sla);

    int count();
}
