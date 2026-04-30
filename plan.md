# Plano de implementação — Chain of Responsibility + Flyweight + PPTX

## 1) Objetivo geral
Entregar um trabalho com:
- Projeto 1 (Java): apenas padrão **Chain of Responsibility**.
- Projeto 2 (Java): apenas padrão **Flyweight**.
- Slides em `md` (roteiro) e em `.pptx`.
- Estrutura simples para demo em sala (~10 minutos).

## 2) Estrutura de diretórios esperada
```text
repo/
  chain-of-responsibility/
    pom.xml
    README.md
    src/main/java/org/example/Main.java
  flyweight/
    pom.xml
    README.md
    src/main/java/org/example/Main.java
  slides/
    roteiro-apresentacao.md
    apresentacao-padroes.pptx
  GITHUB-PUBLISH.md
```

## 3) Requisitos funcionais por projeto

### 3.1 Chain of Responsibility
Implementar um exemplo de help desk com cadeia:
`Bot -> N1 -> N2 -> Gerente`

**Critérios:**
- `Handler` abstrato com `setNext` e `handle`.
- Handlers concretos resolvem ou encaminham.
- `Main` cria cadeia e dispara 3-4 tickets.

**Resultado esperado no console:**
- Ticket simples resolvido pelo Bot.
- Ticket intermediário resolvido por N1/N2.
- Ticket crítico chega ao Gerente.

### 3.2 Flyweight
Implementar exemplo com compartilhamento de tipo de ticket.

**Critérios:**
- `TicketType` (intrínseco): categoria, prioridade, SLA.
- `TicketTypeFactory` com cache (`Map`) e `get(...)`.
- `Ticket` (extrínseco): id, cliente, descrição, referência ao `TicketType`.
- `Main` cria tickets reaproveitando tipo repetido.

**Resultado esperado no console:**
- Exibição dos tickets.
- Prova de reuso de tipo.
- `count()` do factory menor que total de tickets.

## 4) Requisitos técnicos (Java/Maven)
- Java 17.
- `pom.xml` mínimo com `maven.compiler.source/target = 17`.
- `exec-maven-plugin` para rodar via Maven.
- Código curto e didático em `Main.java`.

## 5) Requisitos de README por projeto
Cada README deve conter:
1. Título do projeto.
2. Comandos para executar.
3. Seção "O que demonstra" com 2 bullets.

## 6) Plano dos slides (`slides/roteiro-apresentacao.md`)
Criar 10 slides:
1. Tema e contexto.
2. Motivação do Chain.
3. Estrutura/participantes do Chain.
4. Código curto do Chain.
5. Motivação do Flyweight.
6. Estrutura/participantes do Flyweight.
7. Código curto do Flyweight.
8. Consequências (prós/contras).
9. Roteiro da demo.
10. Encerramento.

## 7) Geração do `.pptx`
Criar `slides/apresentacao-padroes.pptx` com o mesmo conteúdo do roteiro.

**Estratégia preferencial:**
- Usar `python-pptx` se disponível.

**Fallback:**
- Gerar `.pptx` por OpenXML mínimo (zip + XMLs), com títulos e bullets essenciais.

## 8) Publicação e entrega
Criar `GITHUB-PUBLISH.md` com:
- Como adicionar remoto.
- Como fazer push (`main` ou `work`).
- Opção de separar em dois repositórios.

Exemplo:
```bash
git remote add origin https://github.com/USUARIO/REPO.git
git branch -M main
git push -u origin main
```

## 9) Checklist de validação final
- [ ] Estrutura de pastas correta.
- [ ] Ambos `Main.java` compilam e rodam com `javac/java`.
- [ ] Chain mostra encaminhamento na cadeia.
- [ ] Flyweight mostra reuso e contagem do cache.
- [ ] `roteiro-apresentacao.md` criado com 10 slides.
- [ ] `.pptx` válido (testar com `unzip -t`).
- [ ] `GITHUB-PUBLISH.md` criado.
- [ ] ZIP final do projeto gerado (opcional).

## 10) Critérios de qualidade
- Código curto e fácil de explicar.
- Nomes claros (`BotHandler`, `TicketTypeFactory`, etc.).
- Saída de console didática.
- Slides objetivos.

