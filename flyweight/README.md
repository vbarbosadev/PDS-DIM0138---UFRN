# Flyweight

Exemplo didático de central de tickets com compartilhamento de tipos repetidos.

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

- `TicketType` define o contrato do flyweight.
- `AbstractTicketType` concentra o estado intrínseco compartilhado.
- `SharedTicketType` representa a implementação concreta reutilizada.
- `TicketTypeFactory` define o contrato do factory, e `CachedTicketTypeFactory` faz o cache das instâncias.
- `Ticket` mantém o estado extrínseco e referencia o contrato `TicketType`.

## Como funciona dentro do projeto

Quando o projeto inicia, `Main` cria um `CachedTicketTypeFactory`. Esse factory é o responsável por decidir se um tipo de ticket já existe no cache ou se precisa criar um novo.

No projeto, os dados foram separados em dois grupos:

- Estado intrínseco, que pode ser compartilhado:
  `categoria`, `prioridade` e `SLA`.
- Estado extrínseco, que muda de objeto para objeto:
  `id`, `cliente` e `descricao`.

O fluxo acontece assim:

1. `Main` pede ao factory um tipo com `factory.get(...)`.
2. `CachedTicketTypeFactory` monta uma chave com categoria, prioridade e SLA.
3. Se essa chave já estiver no `Map`, ele devolve a mesma instância de `TicketType`.
4. Se não estiver, ele cria um novo `SharedTicketType`, guarda no cache e devolve essa instância.
5. Cada `Ticket` recebe seu estado extrínseco e uma referência para o `TicketType` compartilhado.

Neste projeto, isso significa que tickets diferentes podem reutilizar o mesmo objeto de tipo quando possuem a mesma configuração. Por isso, no final da execução:

- o número total de tickets é maior;
- o número de tipos compartilhados no factory é menor;
- tickets com mesmo tipo mostram a mesma referência de objeto.

Isso evidencia a ideia central do padrão: economizar memória e duplicação reaproveitando o estado que não precisa ser recriado.

## O que demonstra

- Como o estado intrínseco fica concentrado em objetos compartilhados para reduzir duplicação.
- Como o estado extrínseco continua variando em cada ticket sem impedir o reuso do tipo.
