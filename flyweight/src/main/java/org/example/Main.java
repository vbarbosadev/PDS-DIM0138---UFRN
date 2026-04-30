package org.example;

public class Main {

    public static void main(String[] args) {
        TicketTypeFactory factory = new CachedTicketTypeFactory();

        Ticket[] tickets = {
            new Ticket(201, "Loja Azul", "Boleto nao compensou",
                factory.get("Financeiro", "Alta", "4h")),
            new Ticket(202, "Loja Verde", "Erro ao fechar caixa",
                factory.get("Financeiro", "Alta", "4h")),
            new Ticket(203, "Clinica Sol", "Atualizar senha do operador",
                factory.get("Acesso", "Baixa", "24h")),
            new Ticket(204, "Clinica Lua", "Usuario bloqueado apos 3 tentativas",
                factory.get("Acesso", "Baixa", "24h")),
            new Ticket(205, "Mercado Alfa", "Integracao da API falhando",
                factory.get("Infraestrutura", "Critica", "1h"))
        };

        System.out.println("=== Flyweight: Tipos de Ticket Compartilhados ===");
        for (Ticket ticket : tickets) {
            ticket.show();
        }

        System.out.println();
        System.out.println("Total de tickets criados: " + tickets.length);
        System.out.println("Tipos compartilhados no factory: " + factory.count());
        System.out.println("O total de tipos e menor porque varios tickets reaproveitam o mesmo estado intrinseco.");
    }
}
