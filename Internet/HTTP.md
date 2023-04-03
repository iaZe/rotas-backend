# HTTP e a história que você precisa saber

## O que é HTTP?

Começando do começo, o que é HTTP? HTTP é um protocolo de comunicação da camada de aplicação baseado em TCP/IP que padroniza como clientes e servidores se comunicam. Ele define como o conteudo é requisitado e transmitido pela internet. O HTTP depende do TCP/IP para obter solicitações e respostas entre cliente e servidor. Por padrão, a porta TCP 80 é usada, mas outras portas também podem ser usadas. Já o HTTPS é uma versão segura do HTTP, que usa a porta TCP 443.

## HTTP/0.9 - 1991

A primeira versão documentada do HTTP foi [HTTP/0.9](https://www.w3.org/Protocols/HTTP/AsImplemented.html) em 1991. Era o protocolo mais simples de todos os tempos; tendo um único método chamado GET. Se um cliente tivesse que acessar alguma página da web no servidor, ele teria feito a solicitação GET abaixo

```
GET /index.html
```

E a resposta do servidor seria

```
(response body)
<html>
Uma simples página HTML
</html>

(connection closed)
```

Ou seja, o servidor receberia a requisição, responderia com o HTML em resposta e assim que o conteúdo fosse transferido, a conexão seria encerrada. Não havia suporte para cabeçalhos, métodos HTTP, status de resposta, etc.

## HTTP/1.0 - 1996

Em 1996, a versão [HTTP/1.0](https://tools.ietf.org/html/rfc1945) foi lançada e evoluiu muito em relação a versão original.

Ao contrário do HTTP/0.9, que foi projetado apenas para resposta HTML, o HTTP/1.0 agora pode lidar com imagens, arquivos de vídeo, texto simples ou outros tipos de conteúdo. Ele adicionou mais métodos (ou seja, POST e HEAD), os formatos de solicitações/resposta foram alterados, os cabeçalhos foram adicionados e o suporte para conexões persistentes foi adicionado.

Um exemplo de solicitação HTTP/1.0 é mostrado abaixo

```
GET /index.html HTTP/1.0
Host: www.example.com
User-Agent: Mozilla/5.0 (compatible; MSIE5.01; Windows NT)
Accept-Language: pt-br
```

Como você pode ver, juntamente com a solicitação, o cliente enviou suas informações pessoais, tipo de resposta necessária, etc. O servidor, por sua vez, responderia com o seguinte

```
HTTP/1.0 200 OK
Content-Type: text/html
Content-Length: 1024
Expires: Thu, 01 Dec 1994 16:00:00 GMT
Last-Modified: Wed, 08 Jan 1992 23:11:55 GMT
Server: Apache/0.8.4

(response body)
<html>
Uma simples página HTML
</html>

(connection closed)
```

Bem no início da resposta há HTTP/1.0, então há o código de status 200 seguido pela descrição do código de status.

Nessa versão mais recente, os cabeçalhos de solicitação e respostas eram mantidos como codificados em ASCII, mas o corpo da resposta poderia ser de qualquer tipo de conteúdo. Portanto, agora esse servidor pode enviar qualquer conteúdo para o cliente; não muito tempo depois da introdução o termo "Hyper Text" tornouse-se obsoleto. O protocolo de transferência HMTP ou Hypermedia pode ter feito sendio, mas estamos presos com o nome para o resto da vida.

Uma das principais desvantagens do HTTP/1.0 era que você não podia ter várias solicitações por conexão. Ou seja, sempre que um cliente precisar de algo do servidor, ele terá que abrir uma nova conexão TCP e após o atendimento dessa única requisição a conexão será encerrada. E para qualquer próximo requisito, terá que ser em uma nova conexão. Isso é muito ineficiente, caso você visite um site com muitas imagens, por exemplo. Como o servidor fecha a conexão assim que a solicitação é atendida, haverá uma série de conexões separadas onde cada um dos itens será atendido um a um em suas conexões separadas.

## Handshake (Aperto de mão) de três vias

Handshake de três vias em sua forma simples é que todas as conexões TCP começam com um aperto de mão de três vias no qual o cliente e o servidor compartilham uma série de pacotes antes de começar a compartilhar os dados do aplicativo.

<li> SYN - O cliente envia um pacote SYN para o servidor, indicando que ele deseja iniciar uma conexão TCP. </li>
<li> SYN-ACK - O servidor responde com um pacote SYN-ACK, indicando que ele está pronto para iniciar uma conexão TCP. </li>
<li> ACK - O cliente responde com um pacote ACK, indicando que a conexão TCP foi estabelecida. </li>

Após a conclusão do handshake, o compartilhamento de dados entre o cliente e o servidor pode começar. Nota-se que o cliente pode começar a enviar os dados da aplicação assim que enviar o último pacote ACK, mas o servidor ainda terá que aguardar o recebimento do pacote ACK para atender à solicitação. 

<img src="https://i.imgur.com/ohZthqB.png">

No entento, algumas implementações do HTTP/1.0 tentaram superar esse problema introduzindo um novo cabeçalho chamado Coneection: keep-alive, que pretendia dizer ao servidor para não fechar a conexão. Mas, ainda assim, não era tão aplamente suportado e o problema ainda persistia.

Além de ser sem conexão, o HTTP também é um protocolo sem estado, ou seja, o servidor não mantém as informações sobre o cliente e, portanto, cada uma das solicitações deve ter as informações necessárias para que o servidor atenda à solicitação por conta própria, sem nenhuma associação com nenhuma solicitação antiga. E isso adiciona combustível ao fogo, ou seja, além do grande número de conexões que o cliente precisa abrir, ele também precisa enviar alguns dados redundantes em cada solicitação, causando aumento no tráfego de rede.

## HTTP/1.1 - 1997

Após apenas 3 anos de HTTP/1.0, a próxima versão, ou seja, HTTP/1.1 foi lançada em 1999; que fez muitas melhorias em relação ao seu antecessor. As principais melhorias foram:

<li> Novos métodos HTTP (PUT, DELETE, OPTIONS, PATCH) </li>
<li> Identificação do nome do host no cabeçalho seria obrigatório </li>
<li> Suporte para conexões persistentes, ou seja, as conexões por padrão eram mantidas abertas </li>
<!-- Conexões persistentes Conforme discutido acima, no HTTP/1.0 havia apenas uma solicitação por conexão e a conexão era encerrada assim que a solicitação era atendida, o que resultava em problemas agudos de desempenho e latência. O HTTP/1.1 introduziu as conexões persistentes, ou seja, as conexões não eram fechadas por padrão e eram mantidas abertas, o que permitia várias solicitações sequenciais. Para fechar as conexões, o cabeçalho Connection: close deveria estar disponível na requisição. Os clientes geralmente enviam esse cabeçalho na última solicitação para fechar a conexão com segurança. -->
<li> Suporte para pipelining, onde o cliente podia enviar múltiplas requisições ao servidor sem esperar a resposta </li>
<!-- Pipelining Introduziu também o suporte para pipelining, onde o cliente podia enviar múltiplas requisições ao servidor sem esperar a resposta do servidor na mesma conexão e o servidor tinha que enviar a resposta na mesma sequência em que as requisições foram recebidas. Mas como o cliente sabe que este é o ponto em que o download da primeira resposta é concluído e o conteúdo da próxima resposta começa, você pode perguntar! Bem, para resolver isso, deve haver um cabeçalho Content-Length presente que os clientes possam usar para identificar onde a resposta termina e pode começar a aguardar a próxima resposta. -->
<li> Suporte para chunked transfer encoding, onde o servidor pode enviar o conteúdo em partes </li>
<!-- Transferências em Chunked No caso de conteúdo dinâmico, quando o servidor não consegue realmente descobrir o Content-Length quando a transmissão começa, ele pode começar a enviar o conteúdo em pedaços (chunk por chunk) e adicionar o Content-Length para cada chunk quando ele é enviado . E quando todos os blocos são enviados, ou seja, toda a transmissão foi concluída, ele envia um bloco vazio, ou seja, aquele com Content-Length definido como zero para identificar o cliente cuja transmissão foi concluída. Para notificar o cliente sobre a transferência em partes, o servidor inclui o cabeçalho Transfer-Encoding: chunked -->
<li> Autenticação digest e proxy </li>
<li> Cache </li>
<li> Intervalos de bytes </li>
<li> Conjunto de caracteres </li>
<li> Negociação de idiomas </li>
<li> Cookies de cliente </li>
<li> Suporte de compressão aprimorado</li>
<li> Novos códigos de status </li>
<li> E mais </li>

- [As principais diferenças entre HTTP/1.0 e HTTP/1.1](http://www.ra.ethz.ch/cdstore/www8/data/2136/pdf/pd1.pdf)

HTTP/1.1 foi introduzido em 1999 e tem sido um padrão por muitos anos. Embora tenha melhorado muito em relação ao seu antecessor; com a web mudando todos os dias, começou a mostrar sua idade. Carregar uma página hoje exige mais recursos do que nunca. Uma simples página da web hoje tem que abrir mais de 30 conexões. Bem, o HTTP/1.1 tem conexões persistentes, então por que tantas conexões? A razãoi é que no HTTP/1.1 só pode haver uma conexão pendente a qualquer momento. O HTTP/1.1 tentou corrigir isso introduzindo o pipelining, mas não resolveu completamente o problema por causa do bloqueio de cabeçalho, onde usa solicitação lenta ou pesada pode bloquear as solicitações atrasadas e, quando uma solicitação fica presa em um pipeline, terá que esperar os próximos pedidos serem atendidos.

## SPDY - 2009

O Google foi em frente e começou a experimentar protocolos alterativos para tronar a web mais rápida e melhorar a segurança web, reduzindo a latência das páginas da web. Em 2009, eles anunciaram o SPDY.

```
SPDY é uma marca registrada do Google e não é um acrônimo.
```

Foi visto que se continuarmos aumentando a largura de banda, o desempenho da rede aumenta no começo, mas chega um ponto em que não há muito ganho de desempenho. Mas se você fizer o mesmo com a latência, ou seja, se continuarmos diminuindo a latência, haverá um ganho de desempenho constante. Essa foi a ideia central para ganho de desempenho por trás do SPDY, diminuir a latência para aumentar o desempenho da rede.

```
Latência é o atraso, ou seja, quanto tempo leva para os dados trafegarem entre a origem e o destino (em milissegundos) e largura de banda é a quantidade de dados transferidos por segudo (bits por segundo).
```

Os recursos do SPDY incluíam multiplexação, compactação, priorização, segurança, etc. Não entraremos muito em detalhes pois o HTTP/2 é inspirado no SPDY.

Em 2015, o Google anunciou que o SPDY seria substituído pelo HTTP/2 pois não queriam manter dois protocolos diferentes para o mesmo propósito.

## HTTP/2 - 2015

O HTTP/2 foi projetado para transporte de conteúdo de baixa latência. Os principais recursos ou diferenças da versão antiga do HTTP/1.1 são:

<li> Binários em vez de texto </li>
<li> Multiplexação </li>
<!-- Múltiplas solicitações HTTP assíncronas em uma única conexão -->
<li> Compactação de cabeçalho usando HPACK </li>
<li> Servidor push </li>
<!-- Múltiplas respostas para uma única solicitação -->
<li> Priorização de solicitações </li>
<li> Segurança </li>

<br>

<img src="https://i.imgur.com/X1BT5eX.png">

### 1. Protocolo Binário

O HTTP/2 tende a resolver o problema do aumento da latência existente no HTTP/1.x, tornando-o um protocolo binário. Sendo mais fácil de analisar, mas não sendo legível pelo ser humano. Os principais blocos de construção do HTTP/2 são Frames e Streams.

#### Frames e Streams (Fluxos)

As mensagens HTPP agora são compostas por um ou mais frames. Existe um frame HEADERS para os metadados e um frame DATA para o payload e existem vários outros tipos de frames (HEADERS, DATA, PRIORITY...) que você pode verificar através das especificações do [HTTP/2](https://tools.ietf.org/html/rfc7540).

Cada solicitação e resposta HTTP/2 recebe um ID de fluxos exclusivo e é dividido em frames. Os frames nada mais são do que pedaços de binários de dados. Uma coleção de frames é chamada de fluxos. Cada frame possui um fluxos id que identifica o fluxos ao qual pertence e cada frame possui um cabeçalho comum. Além disso, além do fluxos id ser único, vale ressaltar que qualquer solicitação iniciada pelo cliente usa números ímpares e a resposta do servidor tem números pares de fluxos id.

```
Menção ao RST_fluxos, que é um tipo de frame usado para cancelar um fluxos.
```

### 2. Multiplexação

Como o HTTP/2 agora é um protocolo binário, ule usa frames e fluxoss para solicitações e respostas, uma vez que uma conexão TCP é aberta, todos os fluxoss são enviados de forma assíncrona através da mesma conexão sem abrir nenhuma conexão adicional. E por sua vez, o servidor responde da mesma forma assíncrona.

### 3. Compactação de cabeçalho

Quando estamos constantemente acessando o servidor de um mesmo cliente, há muitos dados redundantes que estamos enviando nos cabeçalhos repetidamente e, às vezes, pode haver cookies aumentando o tamanho dos cabeçalhos, o que resulta no uso de largura de banda e latência aumentada. Para superar isso o HTTP/2 trouxe a compactação de cabeçalho.

Ao contrário da solicitação e da resposta, os cabeçalhos não são compactados nos formatos gzip ou compress, existe um mecanismo diferente para compactação de cabeçalho, usando o algoritmo de Huffman, que é um algoritmo de compressão de dados sem perda. Onde o cabeçalho é mantido pelo cliente e servidor e ambos omitem os cabeçalhos redundantes nas próximas solicitações e respostas.

Aproveitando o gancho, os cabeçalhos ainda são os mesmos do HTTP/1.1, exceto pela adicção de alguns pseudo-cabeçalhos, por exemplo `:method`, `:path`, `:scheme` e `:host`.

### 4. Servidor push

O push do servidor é outro recurso do HTTP/2 em que o servidor, sabendo que o cliente está solicitando um recurso, pode enviar um ou mais recursos adicionais ao cliente sem que o cliente os solicite. Isso pode ser usado para melhorar o desempenho da página, por exemplo, se o cliente solicitar uma página HTML, o servidor pode enviar o CSS e o JavaScript associados a essa página HTML.

O push do servidor permite que o servidor diminua as viagens de ida e volta empurrando os dados que ele sabe que o cliente vai exigir. Como isso é feito? O servidor envia um frame especial chamado `PUSH_PROMISE` notificando o cliente que "Estou prestes a enviar um recurso que você pode precisar. Você pode ignorar isso se não precisar." O frame `PUSH_PROMISE` está associado ao fluxos que causou o envio e contém o ID do fluxos no qual o servidor enviará o recurso a ser enviado.

### 5. Priorização de solicitações

Um cliente pode atribuir uma prioridade a um fluxos, incluindo as informações de priorização no frame HEADERS pelo qual um fluxos é aberto. Em qualquer outro momento, o cliente pode enviar um frame `PRIORITY` para alterar a prioridade de um fluxos.

Sem nenhuma informação de prioridade, o servidor pode usar uma política de priorização padrão, por exemplo, priorizar o download de recursos críticos para a renderização da página, como CSS e JavaScript, em relação a outros recursos.

### 6. Segurança

Houve uma extensa discussão sobre se a segurança (através de TLS) deveria ser obrigatória ou não. No final, decidiu-se não torná-la obrigatório. No entando, a maioria dos fornceedores de navegadores recomendam que o HTTP/2 seja usado com TLS.

## HTTP/3 - 2021
<!-- https://http3-explained.haxx.se -->

HTTP/3 é, até o momento, a ultima versão do HTTP. Ele é baseado em QUIC, que é um protocolo de camada de transporte construído sobre o UDP e projetado para substituir o TCP. É um protocolo multiplexado, seguro e baseado em fluxos, projetado para reduzir a latência e aumentar a eficiência da rede.

O QUIC é um protocolo multiplexado, seguro e baseado em fluxos, projetado para reduzir latência e melhorar o desempenho

### 1. Multiplexação

O QUIC é um protocolo multiplexado, ou seja, ele permite que várias conexões sejam abertas em uma única conexão UDP. Isso significa que o QUIC pode enviar e receber dados de várias conexões ao mesmo tempo, sem a necessidade de abrir várias conexões TCP.

### 2. Baseado em stream (fluxos)

QUIC é um protocolo baseado em fluxos, o que significa que os dados são enviados em forma de fluxos. Cada fluxos é identificado por um ID de fluxos exclusivo. O QUIC um único fluxo para enviar e receber dados.

### 3. Datagrama não confiável

O QUIC usa um datagrama não confiável para enviar dados. Isso significa que o QUIC não garante a entrega dos dados. O QUIC usa um mecanismo de reconhecimento de fluxos para garantir que os dados sejam entregues em ordem.


### 4. Migração de conexão

O QUIC suporta migração de conexão, o que significa que uma conexão QUIC pode ser migrada de um endereço IP para outro sem interrupção.

### 5. Recuperação de perdas

O QUIC usa recuperação de perda para se recuperar da perda de pacotes. O QUIC usa uma combinação de controle de congestionamento e recuperação de perda para se recuperar da perda de pacotes.

### 6. Controle de congestionamento

O QUIC usa controle de congestionamento para controlar a taxa na qual os dados são enviados pela rede. Usando uma combinação de controle de congestionamento e recuperação de perda para se recuperar da perda de pacotes.

### 7. Handshake

O QUIC usa um aperto de mão para establecer uma conexão. Usando o TLS 1.3 para estabelecer uma conexão segura entre cliente e servidor semelhante ao HTTP/2

### 8. Compresão de cabeçalho

O QUIC usa compactação de cabeçalho para reduzir o tamanho dos cabeçalhos. O QUIC usa HPACK para compactar os cabeçalhos HTTP.

### 9. Segurança

O QUIC usa TLS 1.3 para estabelecer uma conexão segura entre cliente e servidor. Semelhante ao HTTP/2.

<br>

[Anterior: DNS](/Internet/DNS.md) | [Próximo: Dominios e nomes](/Internet/Dominio.md) 

## Referências

* [cs.fyi](https://cs.fyi/guide/http-in-depth/)
* [RFC Editor](https://www.rfc-editor.org)
* [HTTP/3 Explained](https://http3-explained.haxx.se)

