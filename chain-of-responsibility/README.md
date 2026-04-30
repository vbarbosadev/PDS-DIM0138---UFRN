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

## O que o metodo `resolve(...)` representa

Neste projeto, `resolve(...)` representa o momento em que um elo da cadeia realmente atende a requisição.

No exemplo atual, ele apenas imprime mensagens porque o objetivo do projeto é didático. Mesmo assim, ele já mostra a responsabilidade de cada nível:

- `BotHandler.resolve(...)` trata chamados simples;
- `LevelOneHandler.resolve(...)` trata chamados intermediários;
- `LevelTwoHandler.resolve(...)` trata chamados mais técnicos;
- `ManagerHandler.resolve(...)` trata chamados críticos.

Em um sistema real, `resolve(...)` quase nunca seria só um `println`. Ele normalmente faria a lógica de negócio daquele nível, por exemplo:

- atualizar status do ticket;
- registrar histórico do atendimento;
- consultar banco de dados;
- chamar outro serviço;
- aplicar uma regra automática;
- notificar usuário ou equipe;
- encerrar ou escalar o chamado.

O ponto importante é:

- `handle(...)` decide se aquele elo deve agir ou encaminhar;
- `resolve(...)` executa o trabalho real quando aquele elo é responsável pelo atendimento.

## Como o Chain of Responsibility funciona no geral

O padrão Chain of Responsibility serve para desacoplar quem envia uma requisição de quem realmente vai tratá-la.

Em vez de o cliente fazer algo como:

```text
se for simples, manda para A
se for medio, manda para B
se for critico, manda para C
```

o cliente envia a solicitação para o primeiro elo da cadeia, e a própria cadeia decide quem resolve.

O fluxo geral do padrão é:

1. o cliente envia a requisição para o primeiro handler;
2. o handler atual verifica se consegue tratar;
3. se conseguir, ele resolve;
4. se não conseguir, passa a requisição para o próximo;
5. o processo continua até alguém resolver ou a cadeia acabar.

No projeto:

- `Handler` define o contrato da cadeia;
- `AbstractHandler` implementa o algoritmo comum de encaminhamento;
- os handlers concretos definem suas regras específicas;
- `Ticket` é a requisição trafegando pela cadeia.

## Como isso funciona em um contexto real

Pensando nas classes que já existem, este projeto representa um fluxo simples de service desk.

Cada `Ticket` é um chamado com:

- `id`;
- `description`;
- `severity`.

A `severity` define o nível de complexidade ou urgência do problema:

- `LOW`: problema simples;
- `MEDIUM`: exige suporte operacional básico;
- `HIGH`: exige análise técnica mais profunda;
- `CRITICAL`: exige escalonamento de gestão ou resposta emergencial.

Usando a estrutura atual do projeto, um cenário real seria assim:

1. um cliente abre um chamado;
2. o sistema cria um `Ticket`;
3. esse ticket é enviado ao primeiro ponto de atendimento, aqui representado pelo `BotHandler`;
4. se o bot conseguir resolver, o fluxo termina;
5. se não conseguir, o caso sobe para `LevelOneHandler`;
6. depois pode seguir para `LevelTwoHandler`;
7. por fim, se ainda não houver solução, vai para `ManagerHandler`.

Isso faz sentido em operações reais porque nem todo chamado deve ir direto ao nível mais caro ou mais especializado. A cadeia cria um filtro progressivo:

- casos simples são resolvidos cedo;
- casos intermediários só sobem quando necessário;
- casos críticos chegam aos níveis mais altos já filtrados.

Em um sistema real baseado nessas classes, cada handler poderia ter responsabilidades como:

- `BotHandler`: FAQ, redefinição de senha, respostas automáticas;
- `LevelOneHandler`: checklist padrão, validação inicial, suporte operacional;
- `LevelTwoHandler`: análise de logs, integração, correção técnica;
- `ManagerHandler`: incidentes graves, escalonamento, plano de contingência.

O ganho do padrão é organizacional e estrutural:

- o cliente não precisa conhecer todas as regras de decisão;
- as responsabilidades ficam distribuídas;
- novos níveis podem ser adicionados sem reescrever o cliente;
- a lógica de encaminhamento fica centralizada e reutilizável em `AbstractHandler`.

## O que demonstra

- Como cada handler decide entre resolver a solicitação ou encaminhá-la para o próximo da cadeia.
- Como o cliente envia o ticket para o primeiro handler sem depender de quem de fato o atenderá.
