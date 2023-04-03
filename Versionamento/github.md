# Versionamento com GitHub

## O que é GitHub?

O GitHub é uma plataforma de hospedagem de código para controle de versão e colaboração. Permitindo que você e outras pessoas trabalhem em conjunto em projetos de qualquer lugar.

## Criar um repositório

1. Clique em **+** no canto superior direito da página e selecione **New repository**.
2. Nomeie seu repositório.
3. Na caixa de descrição, escreva uma breve descrição do seu repositório.
4. Selecione Add a README file.
5. Selecione se o seu repositório será público ou privado.
6. Clique em **Create repository**.

## Criar um branch

O Branch permite que você tenha diferentes versões de um repositório de uma vez só. Por exemplo, você pode ter um branch para o desenvolvimento e outro para a produção.

Por padrão, seu repositório tem um branch chamando `main` que é considerado o branch definitivo. Você pode criar branches adicionais com base na `main` no repositório. Você pode usar branches para ter diferentes versões de um projeto de uma só vez. Isso é útil quando você deseja adicionar novas funcionalidades a um projeto sem alterar o código fonte principal. O trabalho feito em diferentes branches não aparecerá no branch principal até que seja feito um `merge`.

<p align="center">
    <img src="https://docs.github.com/assets/cb-23923/mw-1000/images/help/repository/branching.webp" width="400px">
</p>

### Criando um branch

1. Abra seu repositório. 
2. Acima da lista de arquivos, clique no menu `main`.
3. Digite um nome para branch na caixa de texto.
4. Clique em Create branch: `nome` from ´main´

<p align="center">
    <img src="https://docs.github.com/assets/cb-78797/mw-1000/images/help/branches/branch-selection-dropdown.webp" width="400px">
</p>

## Criar um commit

Você pode fazer e salvar as alterações nos arquivos do seu repositório. No GitHub, as alterações salvas são chamadas de commits. Cada commit tem uma mensagem de commit associada, que é uma descrição que explica porque a alteração foi feita.

1. Abra um arquivo e faça uma alteração, por exemplo no README.md
2. Na caixa `Commit changes`, escreva uma mensagem de commit que descreve as mudanças.
3. Clique em Commit changes

## Abrir um pull request

Agora que você tem alterações em um branch com base em `main`, abra uma solicitação de pull.

Os pull requests são o centro da colaboração no GitHub. Ao abrir um pull request, você está propondo suas mudanças e solicitando que alguém analise e faça pul na sua contribuição mesclando no seu branch. Os pull requests mostram diffs, ou seja, a diferença do conteúdo de ambos os branches. As alterações, adicições e substrações são exibidas em cores diferentes.

1. Clique na guia `Pull requests` do repositório.
2. Selecione `New pull request`
3. Na caixa `Compare changes`, selecione o branch que você criou para compará-lo com `main`
4. Veja se as mudanças que você fez na página de comparação e certifique-se que elas são o que você deseja enviar.
5. Clique em `Create pull request`
6. Dê um título ao seu pull request e escreva sobre suas alterações
7. Clique em `Crete pull request`

## Mesclando seu pull request

Nessa etapa, você mesclará o branch do pull request no branch `main`. Depois que você mesclar, as alterações serão incoporadas em `main`.

1. Clique na guia `Pull requests`
2. Abra o Pull request em aberto na aba `Open`
3. Veja se as mudanças feitas na página de comparação e certifique-se que elas são o que você deseja aceitar.
4. Clique em `Merge pull request`
5. Dê um título e descrição
6. Clique em `Confirm merge`

<br>

[Anterior: Git](git.md)

<br>

## Referências

* [GitHub Docs](https://docs.github.com/en)
