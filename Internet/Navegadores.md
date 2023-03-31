# O que são navegadores e como funcionam?

## O que é um navegador?

A principal função de um navegador é apresentar o recurso da WEB que você escolher, solicitando-o ao servidor e exibindo-o na tela. O recurso geralmente é um documento HTML, mas também pode ser um PDF, imagem ou outro tipo de arquivo. A localização do recurso é especificada pelo usuario através de uma URI (Uniform Resource Identifier).

A maneira como o navegador interpreta e exibe arquivos HTML é especificada nas especificações do HTML e do CSS. Essas especificações são mantidas pela W3C (World Wide Web Consortium), que é a organização de padrões para a WEB.

As interfaces de usuário do navegador têm muito em comum umas com as outras. Entre os elementos comuns estão:

* Barra de endereço / barra de pesquisa
* Botões de voltar e avançar
* Botões atualizar e parar
* Opções de favoritos

Curiosamente, a interface do usuário do navegador não é especificada em nenhuma especificação formal, vem apeas de boas práticas e experiência. A especificação HTML5 não define os elementos de interface do usuário do navegador, mas lista alguns elementos comuns. Entre elas estão a barra de endereço. 

## A estrutura de alto nível do navegador

Os principais componentes do navegador são:

* Interface do usuário: esta é a parte visível do navegador. Ela inclui a barra de endereço, o botão de atualização, a barra de status e a janela onde os recursos da WEB são exibidos.
* Mecanismo do navegador: organiza ações entre a interface do usuário e o mecanismo de renderização.
* Mecanismo de renderização: é responsável por exibir o conteúdo da página. Por exemplo, se o conteúdo da página for HTML, o mecanismo de renderização deve interpretar o HTML e CSS e exibir o conteúdo da página.
* Networking: para chamadas de rede, como solicitações HTTP, usando diferentes implementações para diferentes plataformas por trás de uma interface independente da plataforma.
* UI backend: usada para desenhar a interface do usuário do navegador, usando uma implementação diferente em diferentes plataformas.
* JavaScript interpreter: usado para interpretar e executar o JavaScript.
* Armazenamento de dados: esta é uma camada de persistência. O navegador pode armazenar dados localmente no disco, por exemplo, para armazenar os cookies de um site.

<p align="center">
  <img src="https://browserstack.wpenginepowered.com/wp-content/uploads/2022/12/Architecture-of-Web-Browsers-700x564.png" width="400" alt="Estrutura de alto nível do navegador">
<p>

## O que é o mecanismo de renderização?

O mecanismo de renderização é responsável por exibir o conteúdo da página. Por padrão o mecanismo de renderização pode exibir documentos e imagens HTMl e XML. Pode exibir outros tipos de conteúdo, como PDF, usando plugins. 

## Mecanismos de renderização

Diferentes navegadores usam diferentes mecanismos de renderização: Internet Explorer usa o Trident, Firefox usa o Gecko, Safari usa o [WebKit](https://webkit.org/). O Chrome e o Opera usam o Blink, que é um fork do WebKit.

## O fluxo principal

O mecanismo de renderização começará a obter o conteúdo do documento solicitado da camada de rede. Isso geralmente será feito em blocos de 8kB.

Depois disso, este é o fluxo básico do mecanismo de renderização:

<p align="center">
  <img src="https://web-dev.imgix.net/image/T4FyVKpzu4WKF1kBNvXepbi08t52/bPlYx9xODQH4X1KuUNpc.png?auto=format&w=650" width="400" alt="Fluxo principal do mecanismo de renderização">
<p>

O mecanismo de renderização começará a analisar o documento HTML e converterá elementos em nós DOM (Document Object Model) em uma árvore chamada "árvore de conteúdo". O mecanismo de renderização também analisará dados de estilo, tanto CSS quanto elementos de estilo. As informações de estilo junto com as instruções visuais no HTML serão usadas para criar outra arvore, a [árvore de renderização](https://web.dev/howbrowserswork/#render-tree-construction).

A árvore de renderização contém retângulos com atributos visuais como cor e dimensões. Os retângulos estão na ordem certa para serem exibidos na tela.

Após a construção da árvore de renderização ela passa por um processo de ["layout"](https://web.dev/howbrowserswork/#layout). Isso significa dar a cada nó as coordenadas exatas onde ele deve aparecer na tela. A próxima etapa é a pintura, a arvore de renderização será percorrida e cada nó será pintado usando a camada de backend da interface do usuário.

<p align="center">
  <img src="https://web-dev.imgix.net/image/T4FyVKpzu4WKF1kBNvXepbi08t52/S9TJhnMX1cu1vrYuQRqM.png?auto=format&w=650" width="400" alt="Fluxo principal do mecanismo de renderização">
<p>

### Análise

Analisar um documento significa traduzi-lo para uma estrutura que o código pode usar. O resultado da análise é geralmente uma árvore de nós que representam a estrrutura do documento.

## Analisador de HTML

O trabalho do analisador HTML é analisar a marcação HTML em uma árvore de análise

### Definição de gramática HTML

O vocabulário e a sintaxe do HTML são definidos em especificações criadas pela organização W3C.

Existe um formato formal para definir HTML, DTD (Document Type Definition), mas não é uma gramática livre de contexto.

HTML é bastante próximo de XML. Existem muitos analisadores XML disponíveis. Existe uma variação de XML de HTML - XHTML - a diferença é que a abordagem HTML é mais "complacente", ela permite que você omita certas tags (que são adicionadas implicitamente), ou algumas vezes omita as tags de início ou fim, e assim por diante. No geral, é uma sintaxe "suave", em oposição à sintaxe rígida do XML.

### HTML DTD

A definição de HTML está em um formato DTD. Este formato é usado para definir idiomas da família [SGML](https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language) (Standard Generalized Markup Language). O formato contém definições para todos os elementos permitidos, seus atributos e hierarquia. Como vimos anteriormente, o HTML DTD não forma uma gramática livre de contexto.

### DOM

A árvore de saída ("árovre de análise") é uma árvore de elementos DOM e nós de atributos. É a apresentação do objeto do documento HTML e a interface dos elementos HTML para o mundo externo, como o JavaScript.

O DOM tem uma relação quase um-para-um com a marcação. Por exemplo
    
```
<html>
  <body>
    <h1>Olá mundo!</h1>
  </body>
</html>
```

Essa marcação HTML é convertida em uma árvore DOM como essa:
    
<p align="center">
  <img src="https://web-dev.imgix.net/image/T4FyVKpzu4WKF1kBNvXepbi08t52/DNtfwOq9UaC3TrEj3D9h.png?auto=format&w=439" width="400" alt="Fluxo principal do mecanismo de renderização">
<p>

Assim como o HTML, o DOM é especificado pela W3C. Consulte a [especificação DOM](https://www.w3.org/DOM/DOMTR). É uma especificação genérica para manipulação de documentos. As definicões de HTML podem ser encontradas em [HTML DOM](www.w3.org/TR/2003/REC-DOM-Level-2-HTML-20030109/idl-definitions.html).

## Analisador de CSS

Ao contrário do HTML, o CSS é uma gramática livre de contexto e pode ser analisada usando os tipos de analisadores descritos na introdução. Na verdade, a [especificação CSS](https://www.w3.org/TR/CSS2/grammar.html) define o léxico e a gramática sintática do CSS.

## Construção da árvore de renderização

Enquanto a árvore DOM está sendo construída, o navegador constrói outra árvore, a arvore de renderização. Essa árvore é de elementos visuais na ordem em que serão exibidos. É a representação visual do documento. O objetivo dessa árvore é permitir a pintura do conteúdo em sua ordem correta.

A árvore de renderização é construída a partir da árvore DOM. Cada nó DOM é convertido em um nó de renderização. A árvore de renderização é uma árvore de retângulos. Cada retângulo tem atributos visuais como cor e dimensões. Os retângulos estão na ordem correta para serem exibidos na tela.

## Disposição

Quando o renderizador é criado e adicionado à árvore, ele não tem posição e tamanho. O cálculo desses valores é chamado de layout ou refluxo.

O HTML usa um modelo de layout baseado em fluxo, o que significa que na maioria das vezes é possível calcular a geometria em uma única passagem. Os elementos posteriores "no fluxo" normalmente não afetam a geometria dos elementos anteriores "no fluxo", portanto, o layout pode prosseguir da esquerda para a direita e de cima para baixo no documento. Há exceções: por exemplo, tabelas HTML podem exigir mais de uma passagem.

Layout é um processo recursivo. Começa no renderizador raiz, que corresponde ao documento HTML. O layout continua recursivamente através de parte ou de toda a hierarquia do quadro, computando informações geométricas para cada renderizador que o requer.

### O processo de layout

O layout geralmente tem o seguinte padrão:

1. O renderizador pai determina sua própria largura.
2. O pai passa por seus filhos e:
    1. Coloca o renderizador filho (define seu x e y).
    2. Chama o layout do filho, se necessário, que determina sua própria largura e altura.
3. O pai usa as alturas e larguras dos filhos para determinar sua própria altura.
4. Define seu bit sujo como falso.

```
    Bit sujo: Para não fazer um layout completo a cada pequena alteração, os navegadores usam um sistema de bit sujo. Um renderizador que é alterado ou adicionado marca a si mesmo e seus filhos como sujos. 
    Existem dois sinalizadores: "dirty" e "children are dirty", o que significa que, embora o próprio renderizador possa estar OK, ele tem pelo menos um filho que precisa de um layout.
```

### Cálculo de largura

A largura do renderizador é calculada usando a largura do bloco de contêiner, a propriedade CSS `width`.

```
<div style="width: 50%"/>
```

## Pintura

No estágio de pintura, a árvore de renderização é percorrida e o método `paint()` é chamado para exibir o conteúdo na tela. A pintura usa o componente de infraestrutura de interface do usuário.

### A ordem de pintura

[CSS2](https://www.w3.org/TR/CSS21/zindex.html) define a ordem de pintura. Essa é a ordem na qual os elementos são empilhados nos contextos de empilhamento. Essa ordem afeta a pintura, pois as pilhas são pintadas de trás para frente. A ordem de empilhamento de um renderizador de bloco é:

1. Cor de fundo
2. Imagem de fundo
3. Bordas
4. Filhos
5. Cortorno

## Modelo visual CSS2

De acordo com a especificação CSS2, o termo canvas descreve "o espaço onde a estrutura de formatação é renderizada"

A tela é infinita para cada dimensão do espaço, mas os navegadores escolhem uma largura inicial com base nas dimensões da viewport.

### Modelo de caixa CSS 

O [modelo de caixa CSS](https://www.w3.org/TR/CSS2/box.html) descreve as caixas retangulares que são geradas para elementos na árvore do documento e dispostas de acordo com o modelo de formatação visual.

Cada caixa tem uma área de conteúdo e áreas opcionais de preenchimento, borda e margem ao redor.

<p align="center">
  <img src="https://web-dev.imgix.net/image/T4FyVKpzu4WKF1kBNvXepbi08t52/KbqHxGe3HMLM5BbXMcP8.jpg?auto=format&w=571" width="400" alt="Fluxo principal do mecanismo de renderização">
<p>

## Conclusão

O mecanismo de renderização é o coração do navegador. Ele é responsável por converter o HTML e o CSS em pixels na tela. O mecanismo de renderização é um dos componentes mais complexos do navegador. É um sistema de software que é executado em um computador. Ele é responsável por converter o HTML e o CSS em pixels na tela.

<br>

[Anterior: Dominios e nomes](/Internet/Dominio.md) | [Próximo: Hospedagem](/Internet/Hosting.md)

<br>

## Referências

[Google Web.Dev](https://web.dev/howbrowserswork/)
[BrowserStack](https://www.browserstack.com/guide/browser-rendering-engine)
[W3C](https://www.w3.org)
