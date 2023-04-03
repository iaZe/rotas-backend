# Comandos básicos

## Comandos embutidos no terminal

Vamos começar a ver alguns comandos de terminal que já vem prontos para uso no linux

### Básicos

* `cd` - muda o diretório atual para o diretório especificado. Se nenhum diretório for especificado, o diretório atual será o diretório do usuário.
* `mkdir` - cria um novo diretório com o nome especificado.
* `touch` - cria um novo arquivo com o nome especificado.
* `cp` - copia um arquivo ou diretório para outro local.	
* `mv` - move um arquivo ou diretório para outro local.
* `rm` - remove um arquivo
* `rmdir` - remove um diretório vazio.
* `ls` - lista os arquivos e diretórios no diretório atual.
* `curl` - transfere um arquivo de um servidor ou URL.
* `wget` - transfere um arquivo de um servidor ou URL.
* `find` - procura por arquivos e diretórios.
* `cat` - exibe o conteúdo de um arquivo.
* `less` - exibe o conteúdo de um arquivo, mas permite que você navegue pelo arquivo usando as setas do teclado.
* `grep` - procura por uma string em um arquivo ou em um conjunto de arquivos.
* `head` - exibe as primeiras linhas de um arquivo.
* `tail` - exibe as últimas linhas de um arquivo.
* `awk`, `sed`, `tr` - ferramentas para manipular texto.
* `kill` - mata um processo.

### Pipes

O pipe ( `|`) é um operador que permite que você passe a saída de um comando como entrada para outro comando. Por exemplo, `ls | grep .md` irá listar todos os arquivos no diretório atual e passar a saída para o comando `grep`, que irá exibir apenas os arquivos que terminam com `.md`.

### Avançando um pouco

Vamos buscar o conteúdo da página "fetch" do MDN usando curl

Se usarmos:

```
curl https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch
```

Provavelmente teremos uma saída, porque a página foi redirecionada para outra página. Para ver o redirecionamento, podemos usar o comando `curl -L` para seguir o redirecionamento e o comando `grep location` para filtrar a saída para apenas a linha que contém a palavra "location".

```
curl https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch -L -I | grep location
```

Sua saída deve ser algo como:

```
location: /en-US/docs/Web/API/fetch
```

### Outras ferramentas

Aqui estão algumas ferramentas mais avançadas, algumas delas precisam ser instaladas separadamente.

* `npm` - gerenciador de pacotes do Node.js
* `git` - sistema de controle de versão
* `htop` - Um visualizador de processo
* `tldr` - um manual simplificado
* `tree` - exibe uma árvore de diretórios
* `ncdu` - exibe o uso de espaço em disco
* `delta` - Visualizador de diferenças
* `dust` - uma versão mais intuitiva do du
* `duf` - a melhor alternativa ao df
* `broot` - um visualizador de diretório
* `fd` - uma alterativa ao find mais rápido e simples
* `ripgrep` - uma alternativa ao grep mais rápida e simples
* `hyperfine` - um benchmark mais rápido
* `ag` - uma ferramenta de pesquisa para código mais rápida
* `choose`- uma alternativa ao cut que é mais amigável

[Conheça mais ferramentas aqui](https://github.com/ibraheemdev/modern-unix)

<br>

[Anterior: Uso do Terminal](Terminal.md) | [Próximo: Conhecimentos de Sistemas Operacionais](Conhecimentos_do_sistema.md)

<br>

## Referências

* [MDN](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)
* [Modern Unix](https://github.com/ibraheemdev/modern-unix)

