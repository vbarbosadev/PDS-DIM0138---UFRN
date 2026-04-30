# Chain of Responsibility

Exemplo didático de help desk com a cadeia `Bot -> N1 -> N2 -> Gerente`.

## Como executar

```bash
mvn compile exec:java
```

Opcionalmente, se `javac` e `java` 17+ estiverem configurados no `PATH`:

```bash
javac -d out src/main/java/org/example/*.java
java -cp out org.example.Main
```

## Estrutura do padrão

- `Handler` define o contrato da cadeia.
- `AbstractHandler` concentra o fluxo comum de encaminhamento.
- `BotHandler`, `LevelOneHandler`, `LevelTwoHandler` e `ManagerHandler` implementam as decisões concretas.
- `Ticket` e `Severity` representam a requisição processada pela cadeia.

## Como funciona dentro do projeto

Quando o projeto inicia, `Main` cria os objetos `BotHandler`, `LevelOneHandler`, `LevelTwoHandler` e `ManagerHandler` e monta a cadeia nesta ordem:

```text
Bot -> N1 -> N2 -> Gerente
```

Depois disso, `Main` cria alguns `Ticket` com níveis diferentes de severidade e envia todos para o primeiro elo da cadeia, que é o `BotHandler`.

O fluxo acontece assim:

1. `Main` chama `bot.handle(ticket)`.
2. `AbstractHandler` executa o algoritmo comum da cadeia.
3. Cada handler concreto verifica se consegue atender o ticket com `canHandle(ticket)`.
4. Se conseguir, resolve com `resolve(ticket)`.
5. Se não conseguir, encaminha para o próximo handler com `next.handle(ticket)`.

Neste projeto, a responsabilidade de cada classe é:

- `BotHandler`: resolve tickets `LOW`.
- `LevelOneHandler`: resolve tickets `MEDIUM`.
- `LevelTwoHandler`: resolve tickets `HIGH`.
- `ManagerHandler`: resolve tickets `CRITICAL`.

Isso mostra a principal ideia do padrão: `Main` conhece apenas o primeiro ponto de entrada da cadeia, mas não precisa decidir manualmente quem vai tratar cada caso.

## O que demonstra

- Como cada handler decide entre resolver a solicitação ou encaminhá-la para o próximo da cadeia.
- Como o cliente envia o ticket para o primeiro handler sem depender de quem de fato o atenderá.
