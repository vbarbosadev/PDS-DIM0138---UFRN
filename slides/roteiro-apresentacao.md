# Apresentação de Padrões de Projeto

Tempo alvo: 10 minutos  
Padrões estudados pelo grupo: `Chain of Responsibility` e `Flyweight`  
Observação para a apresentação: o grupo deve estar pronto para apresentar qualquer um dos dois padrões sorteados, mas os slides já cobrem os dois para estudo e ensaio.

---

## Slide 1 — Tema e contexto
- Disciplina: Padrões de Projeto
- Grupo estudou dois padrões GoF: `Chain of Responsibility` e `Flyweight`
- Cada integrante participa da explicação e da demonstração
- O objetivo é mostrar quando usar, como funciona e um exemplo executável em Java

**Fala sugerida:** abertura, contexto do trabalho e ordem da apresentação.

---

## Slide 2 — Chain of Responsibility: Motivation e Applicability
- **Motivation:** evitar muitos `if/else` concentrando toda a decisão em um único ponto do sistema
- **Problema típico:** uma solicitação pode ser tratada por diferentes níveis de atendimento
- **Applicability:** fluxos de suporte, aprovação, validação, autenticação e processamento em etapas
- **Ideia central:** o cliente envia a requisição para o primeiro elo, e a cadeia decide quem resolve

---

## Slide 3 — Chain of Responsibility: Structure, Participants e Collaborations
- **Structure:** `Cliente -> Bot -> N1 -> N2 -> Gerente`
- **Participants:**
  - `Handler`: define `setNext()` e `handle()`
  - `BotHandler`, `LevelOneHandler`, `LevelTwoHandler`, `ManagerHandler`: handlers concretos
  - `Ticket`: objeto que carrega a solicitação
- **Collaborations:** cada handler verifica se consegue resolver; se não, encaminha para o próximo

---

## Slide 4 — Chain of Responsibility: Consequences e código
- **Consequences positivas:** baixo acoplamento entre cliente e atendente final; fluxo extensível
- **Consequences negativas:** cadeia muito longa pode dificultar rastreamento e depuração
- Exemplo da demo:

```java
bot.setNext(n1).setNext(n2).setNext(gerente);
bot.handle(new Ticket(101, "Resetar senha", Severity.LOW));
bot.handle(new Ticket(104, "Vazamento de dados", Severity.CRITICAL));
```

- Resultado esperado:
  - ticket simples resolvido pelo Bot
  - ticket intermediário resolvido por N1 ou N2
  - ticket crítico chega ao Gerente

---

## Slide 5 — Flyweight: Motivation e Applicability
- **Motivation:** evitar repetição de dados iguais em muitos objetos parecidos
- **Problema típico:** vários tickets usam a mesma categoria, prioridade e SLA
- **Applicability:** sistemas com muitos objetos pequenos e grande volume de estado compartilhável
- **Ideia central:** separar estado intrínseco compartilhável do estado extrínseco específico de cada objeto

---

## Slide 6 — Flyweight: Structure, Participants e Collaborations
- **Structure:** `Cliente cria Ticket -> Ticket usa TicketType -> TicketTypeFactory reaproveita instâncias`
- **Participants:**
  - `TicketType`: estado intrínseco (`categoria`, `prioridade`, `SLA`)
  - `Ticket`: estado extrínseco (`id`, `cliente`, `descrição`)
  - `TicketTypeFactory`: cache de tipos compartilhados
- **Collaborations:** antes de criar um tipo novo, o sistema consulta o factory para reaproveitar um existente

---

## Slide 7 — Flyweight: Consequences e código
- **Consequences positivas:** reduz duplicação e uso de memória; centraliza dados compartilhados
- **Consequences negativas:** exige separar bem o que é intrínseco e extrínseco
- Exemplo da demo:

```java
factory.get("Financeiro", "Alta", "4h");
factory.get("Financeiro", "Alta", "4h");
factory.get("Acesso", "Baixa", "24h");
```

- Resultado esperado:
  - vários tickets exibidos no console
  - referências de objeto repetidas para tipos iguais
  - `factory.count()` menor que o total de tickets

---

## Slide 8 — Roteiro da demonstração
- Executar primeiro o projeto `chain-of-responsibility`
- Mostrar a criação da cadeia e o encaminhamento dos tickets
- Executar depois o projeto `flyweight`
- Mostrar o cache do factory e o reaproveitamento dos tipos
- Deixar o código completo no SIGAA e usar os slides apenas como apoio visual

---

## Slide 9 — Comparação rápida entre os padrões
- `Chain of Responsibility` organiza **quem processa** uma solicitação
- `Flyweight` organiza **como compartilhar** dados repetidos entre muitos objetos
- O primeiro foca em fluxo e encaminhamento
- O segundo foca em economia de recursos e reaproveitamento
- Os dois exemplos usam cenários de suporte para facilitar a explicação em sala

---

## Slide 10 — Encerramento e divisão da fala
- Integrante 1: abertura, motivação e aplicabilidade do Chain
- Integrante 2: estrutura, participantes e consequências do Chain
- Integrante 3: motivação, aplicabilidade e estrutura do Flyweight
- Integrante 4: demo, comparação final e respostas a perguntas
- Mensagem final: os padrões ajudam a resolver problemas recorrentes com soluções reutilizáveis e explicáveis

---

## Comandos da demo

### Chain of Responsibility
```bash
cd chain-of-responsibility
mvn compile exec:java
```

### Flyweight
```bash
cd flyweight
mvn compile exec:java
```
