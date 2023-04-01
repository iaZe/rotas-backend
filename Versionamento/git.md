# Versionamento com Git

## O que é controle de versão?

O controle de versão, também conhecido como controle de origem, é a prática de restrear e gerenciar alterações no código do software. Os sistemas de controle de versão são ferramentas de software que ajudam as equips a gerenciar alterações no código-fonte ao longo do tempo.

O software de controle de versão acompanha cada modificação no código em um tipo especial de banco de dados. Se um erro for cometido, os desenvolvedores podem voltar no tempo e comparar as versões anteriores do código para ajudar a corrigir o erro.

## O que é Git?

De longe, o sistema de controle de versão moderno mais usado no mundo hoje é o Git. O Git é um projeto de código aberto e mantido ativamente, originalmente desenvolvido por Linus Torvalds, o criador do Linux. Um número impressionante de projetos de software depende do Git para controle de versão, incluindo projetos comerciais e de código aberto.

### Desempenho

As características de desempenho bruto do Git são muito fortes em comparação com outros sistemas de controle de versão. O Git é projetado para lidar com grandes projetos de software, como o Linux, que tem mais de 26 milhões de linhas de código. O Git também é projetado para lidar com grandes equipes de desenvolvimento, com centenas ou milhares de desenvolvedores contribuindo para um único projeto.

### Segurança

O Git foi projetado com a integridade do código-fonte gerenciado como prioridade máxima. O conteúdo dos arquivos, bem como as verdadeiras relações entre arquivos e diretórios, versões, tags e commits, todos esses objetos no repositório Git são protegidos por um algoritmo de hash criptograficamente seguro chamado SHA1. Isso protege o código e o histórico de alterações contra alteração acidental e maliciosa e garante um histórico totalmente rastreável.

### Flexibilidade

O Git é projetado para ser flexível em vários aspectos: no suporte a vários tipos de fluxos de trabalho de desenvolvimento não linear, em sua eficiência em projetos pequenos e grandes e em sua compatibilidade com muitos sistemas e protocolos existentes.

## Instalando o Git

Vou focar somente na instalação do Git no Windows, mas você pode encontrar mais informações sobre outras plataformas [aqui](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Windows

Para instalar o Git no Windows, você pode baixar o instalador [aqui](https://git-scm.com/download/win). Ou fazer de uma maneira muito mais interessante. Através do winget (Windows Package Manager).


Powershell
```
winget install --id Git.Git -e --source winget
```

Depois de instalado, abra um Prompt de Comando (ou Git Bash) e configure seu nome de usuário e endereço de e-mail. Isso é importante porque cada commit no Git usa essas informações, e elas são imutáveis:

```
git config --global user.name "Seu Nome"
git config --global user.email "seunome@email.com"
```

## Usando o Git

### Criando um repositório

Vamos ver alguns comando básicos do Git. Primeiro, vamos criar um repositório Git. Para criar um repositório Git, você pode usar o comando `git init` em um diretório.

```
git init <diretorio>
```

### Clonando um repositório

Para clonar um repositório, você pode usar o comando `git clone`:

```
git clone <url>
```

git clone é usado para criar uma cópia de repositórios remotos. Nesse exemplo, usaremos o protocolo Git SSH. Os URLs do Git SSH seguem um modelo

```
git@hostname:username/repository.git

git@github.com:iaZe/Estudos.git

- git: o protocolo Git SSH
- hostname: github.com
- username: iaZe
- repository: Estudos
```

### Salvando alterações

Para salvar alterações no repositório, você pode usar o comando `git add`:

```
git add <arquivo>
```

Logo após, você pode usar o comando `git commit`:

```
git commit -m "Mensagem"
```

```
iaZe@DESKTOP MINGW64 ~/Desktop/test (master)
$ git add primeiro_add.txt

iaZe@DESKTOP MINGW64 ~/Desktop/test (master)
$ git commit -m "Adicionando o TXT ao repositório"
[master (root-commit) 00x00x0] Adicionando o TXT ao repositório
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 primeiro_add.txt
```

Depois disso, sua adicção terá sido adicionada ao histórico e rastreará futuras mudanças no arquivo.

### Verificando o status

Para verificar o status do repositório, você pode usar o comando `git status`:

```
git status
```

```
iaZe@DESKTOP MINGW64 ~/Desktop/test (master)
$ git status
On branch master
nothing to commit, working tree clean
```

Com isso você pode ver se há arquivos que ainda não foram adicionados ao repositório. Se você quiser ver quais arquivos foram alterados, mas ainda não foram adicionados ao repositório, você pode usar o comando `git diff`:

```
git diff
```

```
iaZe@DESKTOP MINGW64 ~/Desktop/test (master)
$ git diff
diff --git a/primeiro_add.txt b/primeiro_add.txt
index 0000000..0000000
--- a/primeiro_add.txt
+++ b/primeiro_add.txt
@@ -0,0 +1 @@
+Teste
```

### Enviando alterações

Caso você tenha criado um repositório local, você pode usar o comando `git remote add` para adicionar um repositório remoto:

```
git remote add <repositorio> <url>
```

Caso você tenha clonado um repositório ou tenha adicionado um repositório remoto, você pode usar o comando `git push` para enviar alterações para o repositório remoto:

```
git push <repositorio> <branch>
```

E tera algo parecido com isso:

```
iaZe@DESKTOP MINGW64 ~/Desktop/test (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 220 bytes | 220.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:iaZe/Estudos.git
 * [new branch]      master -> master
```

## Resumo

Demonstramos um pouco sobre o Git e como ele funciona. Também vimos como criar ou clonar repositórios e fazer alterações nele

<br>

[Proximo: Github](/github.md)

<br>

## Referências

* [Atlassian Bitbucket](https://www.atlassian.com/br/git/tutorials/what-is-version-control)
* [Git - Documentação Oficial](https://git-scm.com/doc)
