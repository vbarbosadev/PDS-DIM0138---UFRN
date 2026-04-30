package org.example;

import java.util.LinkedHashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        TicketTypeFactory factory = new TicketTypeFactory();

        Ticket[] tickets = {
            new Ticket(201, "Loja Azul", "Boleto não compensou",
                factory.get("Financeiro", "Alta", "4h")),
            new Ticket(202, "Loja Verde", "Erro ao fechar caixa",
                factory.get("Financeiro", "Alta", "4h")),
            new Ticket(203, "Clínica Sol", "Atualizar senha do operador",
                factory.get("Acesso", "Baixa", "24h")),
            new Ticket(204, "Clínica Lua", "Usuário bloqueado após 3 tentativas",
                factory.get("Acesso", "Baixa", "24h")),
            new Ticket(205, "Mercado Alfa", "Integração da API falhando",
                factory.get("Infraestrutura", "Crítica", "1h"))
        };

        System.out.println("=== Flyweight: Tipos de Ticket Compartilhados ===");
        for (Ticket ticket : tickets) {
            ticket.show();
        }

        System.out.println();
        System.out.println("Total de tickets criados: " + tickets.length);
        System.out.println("Tipos compartilhados no factory: " + factory.count());
        System.out.println("O total de tipos é menor porque vários tickets reaproveitam o mesmo estado intrínseco.");
    }



    record TicketType(String category, String priority, String sla) {
        public String summary() {
            return category + " | prioridade " + priority + " | SLA " + sla;
        }
    }

    record Ticket(int id, String customer, String description, TicketType type) {
        public void show() {
            System.out.printf("Ticket #%d | Cliente: %s%n", id, customer);
            System.out.println("  Descrição: " + description);
            System.out.println("  Tipo compartilhado: " + type.summary());
            System.out.println("  Referência do tipo: " + System.identityHashCode(type));
            System.out.println();
        }
    }

    static class TicketTypeFactory {
        private final Map<String, TicketType> cache = new LinkedHashMap<>();

        public TicketType get(String category, String priority, String sla) {
            String key = category + "|" + priority + "|" + sla;
            return cache.computeIfAbsent(key, ignored -> {
                System.out.println("Criando novo TicketType para " + key);
                return new TicketType(category, priority, sla);
            });
        }

        public int count() {
            return cache.size();
        }
    }
}
