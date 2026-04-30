# Chain of Responsibility

Exemplo didático de help desk com a cadeia `Bot -> N1 -> N2 -> Gerente`.

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

- Como cada handler decide entre resolver a solicitação ou encaminhá-la para o próximo da cadeia.
- Como o cliente envia o ticket para o primeiro handler sem depender de quem de fato o atenderá.
