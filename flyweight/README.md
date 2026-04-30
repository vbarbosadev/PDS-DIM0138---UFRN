# Flyweight

Exemplo didático de central de tickets com compartilhamento de tipos repetidos.

## Como executar

```bash
mvn compile exec:java
```

Opcionalmente, se `javac` e `java` 17+ estiverem configurados no `PATH`:

```bash
javac -d out src/main/java/org/example/Main.java
java -cp out org.example.Main
```

## O que demonstra

- Como o estado intrínseco fica concentrado em objetos compartilhados para reduzir duplicação.
- Como o estado extrínseco continua variando em cada ticket sem impedir o reuso do tipo.
