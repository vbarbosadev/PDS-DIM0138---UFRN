package org.example;

public record Ticket(int id, String customer, String description, TicketType type) {

    public void show() {
        System.out.printf("Ticket #%d | Cliente: %s%n", id, customer);
        System.out.println("  Descricao: " + description);
        System.out.println("  Tipo compartilhado: " + type.summary());
        System.out.println("  Referencia do tipo: " + System.identityHashCode(type));
        System.out.println();
    }
}
