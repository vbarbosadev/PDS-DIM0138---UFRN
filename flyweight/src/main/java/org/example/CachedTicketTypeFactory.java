package org.example;

import java.util.LinkedHashMap;
import java.util.Map;

public class CachedTicketTypeFactory implements TicketTypeFactory {
    private final Map<String, TicketType> cache = new LinkedHashMap<>();

    @Override
    public TicketType get(String category, String priority, String sla) {
        String key = category + "|" + priority + "|" + sla;
        return cache.computeIfAbsent(key, ignored -> {
            System.out.println("Criando novo TicketType para " + key);
            return new SharedTicketType(category, priority, sla);
        });
    }

    @Override
    public int count() {
        return cache.size();
    }
}
