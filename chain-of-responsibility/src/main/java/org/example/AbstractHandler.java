package org.example;

public abstract class AbstractHandler implements Handler {
    private Handler next;

    @Override
    public Handler setNext(Handler next) {
        this.next = next;
        return next;
    }

    @Override
    public final void handle(Ticket ticket) {
        if (canHandle(ticket)) {
            resolve(ticket);
            return;
        }

        if (next == null) {
            System.out.println(name() + " nao encontrou proximo atendente.");
            return;
        }

        System.out.println(name() + " encaminhou para " + next.name() + ".");
        next.handle(ticket);
    }

    protected abstract boolean canHandle(Ticket ticket);

    protected abstract void resolve(Ticket ticket);
}
