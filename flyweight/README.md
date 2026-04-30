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

## O que é o SLA neste projeto

`SLA` significa **Service Level Agreement**, ou **Acordo de Nível de Serviço**.

Neste projeto, o SLA representa o tempo esperado para atendimento ou resolução de um tipo de ticket. Ele aparece como parte do estado compartilhado do `TicketType`, por exemplo:

- `4h`: esse tipo de ticket deve ser tratado em até 4 horas;
- `24h`: esse tipo de ticket tem prazo mais folgado;
- `1h`: esse tipo de ticket é mais urgente e exige resposta mais rápida.

No código atual, o SLA é apenas um dado textual usado para demonstrar o padrão. Em um sistema real, ele poderia influenciar:

- prioridade de fila;
- alertas automáticos;
- prazo para escalonamento;
- indicadores de atraso;
- regras de atendimento por equipe.

## Como a memória funciona aqui

Sem Flyweight, cada `Ticket` carregaria uma cópia própria de:

- `category`;
- `priority`;
- `sla`.

Isso significa que, se existirem 10 mil tickets do mesmo tipo, o sistema também criaria 10 mil objetos com os mesmos dados repetidos.

Com Flyweight, esses dados repetidos são extraídos para um objeto compartilhado:

- `SharedTicketType` guarda o estado intrínseco;
- `Ticket` guarda só o estado extrínseco e uma referência para esse tipo;
- `CachedTicketTypeFactory` garante que tipos iguais apontem para a mesma instância.

Então, em vez de:

```text
Ticket 1 -> copia completa do tipo
Ticket 2 -> copia completa do tipo
Ticket 3 -> copia completa do tipo
```

o projeto passa a funcionar assim:

```text
Ticket 1 -> referencia para um TicketType compartilhado
Ticket 2 -> referencia para o mesmo TicketType
Ticket 3 -> referencia para o mesmo TicketType
```

O impacto na memória vem daí:

- menos objetos duplicados;
- menos repetição de strings e estruturas iguais;
- menor custo total quando a quantidade de objetos cresce muito.

No exemplo atual, a economia é pequena porque há poucos tickets. O valor do padrão aparece de verdade quando o sistema tem centenas, milhares ou milhões de objetos semelhantes.

## Como o Flyweight funciona no geral

O padrão Flyweight serve para reduzir custo de memória quando muitos objetos têm uma parte grande do estado repetida.

Ele faz isso separando os dados em dois grupos:

- **estado intrínseco**: parte que pode ser compartilhada entre vários objetos;
- **estado extrínseco**: parte que continua sendo individual de cada objeto.

O fluxo geral do padrão é:

1. o cliente pede um flyweight ao factory;
2. o factory verifica se já existe uma instância compatível;
3. se existir, reutiliza;
4. se não existir, cria e guarda;
5. os objetos do sistema passam a apontar para esse flyweight compartilhado.

No projeto:

- `TicketType` é o contrato do flyweight;
- `AbstractTicketType` e `SharedTicketType` representam o objeto compartilhável;
- `TicketTypeFactory` define o contrato de obtenção;
- `CachedTicketTypeFactory` implementa o reuso com `Map`;
- `Ticket` representa o objeto final que usa o flyweight.

## Como isso funcionaria em um contexto real

Pensando nas classes que já existem, este projeto pode ser lido como uma central de suporte técnico ou service desk.

Cada `Ticket` representa uma ocorrência específica aberta por um cliente:

- um cliente tem seu próprio `id`;
- cada chamado tem sua própria `descricao`;
- cada ocorrência pertence a um cliente diferente.

Mas muitos tickets compartilham a mesma configuração operacional. Por exemplo:

- vários tickets podem ser da categoria `Financeiro`;
- vários podem ter prioridade `Alta`;
- vários podem ter `SLA` de `4h`.

Nesse cenário, não faz sentido recriar sempre o mesmo bloco de dados. Então:

- `CachedTicketTypeFactory` atua como um catálogo de tipos já conhecidos;
- `SharedTicketType` representa um perfil padrão de atendimento;
- `Ticket` aponta para esse perfil em vez de copiar tudo.

Em um sistema real, um `TicketType` poderia representar algo como:

- categoria do chamado;
- nível de prioridade;
- prazo de atendimento;
- equipe responsável;
- regras de escalonamento;
- cor ou etiqueta usada na interface;
- política de notificação.

Já cada `Ticket` continuaria guardando só o que é específico daquela ocorrência:

- número do chamado;
- cliente;
- descrição do problema;
- horário de abertura;
- técnico responsável no momento;
- observações e histórico.

Usando as classes deste projeto como base, o raciocínio seria:

1. `Main` simula a entrada de vários chamados.
2. Para cada chamado, o sistema consulta `CachedTicketTypeFactory`.
3. Se já existir um tipo `Financeiro|Alta|4h`, o factory devolve a mesma instância.
4. O novo `Ticket` nasce com seus próprios dados, mas compartilhando esse tipo.
5. Isso reduz duplicação e centraliza a definição do comportamento comum daquele perfil.

Na prática, o Flyweight é útil quando:

- existem muitos objetos;
- grande parte deles repete os mesmos dados;
- esses dados repetidos podem ser isolados com segurança;
- compartilhar esses dados reduz custo sem quebrar o modelo do domínio.

## O que demonstra

- Como o estado intrínseco fica concentrado em objetos compartilhados para reduzir duplicação.
- Como o estado extrínseco continua variando em cada ticket sem impedir o reuso do tipo.
