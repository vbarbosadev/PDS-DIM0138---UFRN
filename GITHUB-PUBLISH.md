# Publicação no GitHub

## Opção 1: publicar tudo em um único repositório

```bash
git init
git add .
git commit -m "Entrega do trabalho de padrões"
git remote add origin https://github.com/USUARIO/REPO.git
git branch -M main
git push -u origin main
```

Se a branch principal do grupo for `work`, substitua o último bloco por:

```bash
git branch -M work
git push -u origin work
```

## Opção 2: publicar cada padrão em um repositório separado

### Repositório 1: Chain of Responsibility
```bash
cd chain-of-responsibility
git init
git add .
git commit -m "Projeto Chain of Responsibility"
git remote add origin https://github.com/USUARIO/chain-of-responsibility.git
git branch -M main
git push -u origin main
```

### Repositório 2: Flyweight
```bash
cd flyweight
git init
git add .
git commit -m "Projeto Flyweight"
git remote add origin https://github.com/USUARIO/flyweight.git
git branch -M main
git push -u origin main
```

## Sugestão de entrega

- Manter um único repositório simplifica a submissão e o versionamento.
- Separar os projetos só vale a pena se o grupo quiser apresentar ou evoluir cada exemplo de forma independente.
