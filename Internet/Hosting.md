# O que é uma Hospedagem?

## Servidor web

O termo servidor web pode se referir a hardware ou software, ou ambos juntos.

1. Referente ao hardware, um servidor web é um computador que armazena arquivos que compõem os sites e os entrega para o dispositivo do usuário final. Ele pode ser acessado por meio de seu nome de domínio (DNS), como exemplo `google.com`.
2. Referente ao software, um servidor web inclui diversos componentes que controlam como os usuários acessam os arquivos hospedados, no mínimo um servidor HTTP, que é o responsável por interpretar as requisições HTTP e entregar os arquivos solicitados.

<p align="center">
  <img src="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server/web-server.svg" alt="Servidor web" width="400" />
</p>

Para publicar um site, é necessário um servidor web estático ou um dinâmico.

Um servidor web estático consiste em um computador com um servidor HTTP. É chamado de "estático" porque o servidor envia seus arquivos tal como foram criados e armazenados ao navegador. 

Um servidor web dinâmico consiste em um servidor web estático com software adicional, mais comumente um servidor de aplicações e um banco de dados. É chamado de "dinâmico" porque o servidor de aplicativos atualiza os arquivos hospedados antes de enviá-los ao navegador através do servidor HTTP.

## Entrando em detalhes

Para carregar uma página web, como ja foi dito, seu navegador envia uma requisição ao servidor, que busca pelo arquivo requisitado no seu próprio armazenamento. Ao encontrar o arquivo, o servidor realiza a leitura, faz os processos necessários e envia o arquivo para o navegador.

### Hospedagem de arquivos

Primeiro, um servidor web deve armazenar os arquivos que compõem o site. Como todos os documentos HTML, CSS e JavaScript.

Tecnicamente, você poderia hospedar todos esses arquivos em seu próprio computador, mas é muito mais conveniente armazenar todos os arquivos em um servidor dedicado porque:

- Um servidor está sempre ativo
- Está sempre conectado à Internet
- Tem o mesmo endereço de IP sempre
- É mantido por terceiros

Por todos esses motivos, encontrar um bom provedor de hospedagem é uma tarefa importante na criação de um site. <strike>Agora seria um bom momento para um patrocínio.</strike>

### Comunicando através do HTTP

Segundo, um servidor web fornece suporte para [HTTP](/Internet/HTTP.md). O HTTP especifica como transferir hipertexto entre dois computadores. 

O HTTP fornece regras claras sobre como um cliente e um servidor se comunicam.

Em uma hospedagem, o servidor HTTP é responsável por interpretar as requisições HTTP e entregar os arquivos solicitados.

1. Ao receber uma requisição, um servidor HTTP verifica se a URL solicitada corresponde a um arquivo existente.
2. Nesse caso, o servidor da Web envia o conteúdo do arquivo de volta ao navegador. Caso contrário, o servidor verificará se deve gerar um arquivo dinamicamente para a requisição.
3. Se nenhuma dessas opções for possível, o servidor da Web retornará uma mensagem de erro ao navegador, geralmente [`404 Not Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404). É um erro tão comum que alguns web designers criaram páginas de erro personalizadas para substituir a mensagem padrão.

### Conteúdo estático x dinâmico

A grosso modo, um servidor pode servir conteúdo estático ou dinâmico. Lembre-se de que "estático" significa "da forma que está". Sites estáticos são mais fáceis de configurar, então sugerimos que você faça seu primeiro site estático.

O termo "dinâmico" significa que o servidor processa o conteúdo ou gera a partir de um banco de dados. Essa abordagem oferece mais flexibilidade, mas a arquitetura fica mais difícil de configurar, tornando mais desafiador construir um site.

<br> 

[Anterior: Hospedagem](/Internet/Hosting.md) | [Próximo: Aprendendo programação](/Aprendendo_Programacao/)

<br>

## Referências

* [MDN - What is a web server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)