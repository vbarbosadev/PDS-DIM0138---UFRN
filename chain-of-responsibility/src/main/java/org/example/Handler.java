package org.example;

public interface Handler {

    Handler setNext(Handler next);

    void handle(Ticket ticket);

    String name();
}
