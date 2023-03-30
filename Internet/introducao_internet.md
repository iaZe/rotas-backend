# 🌐 Como funciona a Internet

## Introdução à Internet

Antes de entender a internet, precisamos entender as redes. Uma rede é um conjunto de dispositivos conectados uns aos outros. 

Você em sua casa pode pode ter uma rede de computadores e dispositivios. Seu amigo pode ter uma rede de computadores e dispositivos. Todas essas redes quando conectadas formam a internet.

```
A internet é uma rede de redes. 
```

<img href="https://github.com/iaZe/Estudos/img/network.png">

A internet foi desenvolvida no final dos anos 60 pelo Departamento de Defesa dos Estados Unidos como um meio de criar uma rede de comunicação descentralizada que pudesse resistir a um ataque nuclear. Ao longo dos anos evouiu para uma rede comercial e hoje é usada para diversas finalidades.

## Como funciona a internet

Em um alto nível, a internet funciona conectando dispositivos usando protocolos padronizados que garantem a troca de dados e infomações de maneira segura e confiável.

O núcleo da internet é uma rede global de roteadores interconectados, que direcionam o tráfego entre diferentes dispositivos. Quando você envia dados pela internet, eles são divididos em pequenos pacotes que são enviados para o roteador mais próximo. O roteador então encaminha os pacotes para o próximo roteador mais próximo até que eles cheguem ao destino final.

Para garantir que os pacotes cheguem ao destino final, os roteadores usam um protocolo chamado IP (Internet Protocol). O IP é um protocolo de endereçamento que permite que os roteadores identifiquem os pacotes e os encaminhem para o destino correto. Cada dispositivo conectado à internet possui um endereço IP único que é usado para identificá-lo na rede.

Além do IP, a internet também usa um protocolo de transporte chamado TCP (Transmission Control Protocol). O TCP é responsável por garantir que os pacotes cheguem ao destino final e que eles cheguem na ordem correta. O TCP também é responsável por garantir que os pacotes não sejam corrompidos durante o transporte.

## Conceitos básicos e terminologia
<li> Pacote: Um pacote é um bloco de dados que é enviado pela internet. </li>
<li> Roteador: Um roteador é um dispositivo que é usado para encaminhar pacotes entre diferentes redes. </li>
<li> Protocolo: Um protocolo é um conjunto de regras que define como os dispositivos se comunicam. </li>
<li> IP: É um identificador exclusivo atribuído a cada dispositivo em uma rede </li>
<li> TPC: É um protocolo de transporte que é responsável por garantir que os pacotes cheguem ao destino final e que eles cheguem na ordem correta. </li>
<li> UDP: É um protocolo de transporte que é usado para enviar e receber dados da web. </li>
<li> DNS: É um serviço que é usado para converter nomes de domínio em endereços IP. </li>
<li> HTTP: É um protocolo de aplicação que é usado para enviar e receber dados da web. </li>
<li> SSL/TLS: É um protocolo de segurança que é usado para garantir que os dados enviados pela internet sejam criptografados. </li>
<br>
Compreender esses conceitos básicos é importante para entender como a internet funciona.

## O papel dos protocolos na internet

Os protocolos são fundamentais para a comunicação e troca de dados na internet, pois definem as regras para a interação entre os dispositivos.

O IP é responsável por rotear os pacotes de dados para seu destino correto, enquanto o TCP e o UDP são responsáveis por garantir que os pacotes cheguem ao destino final e que eles cheguem na ordem correta. O DNS é um serviço que é usado para converter nomes de domínio em endereços IP e o HTTP é um protocolo de aplicação que é usado para enviar e receber dados da web.

O uso de protocolos padronizados oferece a vantagem de permitir que dispositivos de fabricantes diferentes se comuniquem sem problemas.

É essencial entender os protocolos usados na comunicação pela internet e como eles funcionam juntos para a transferência de dados.

## Noções básicas sobre endereços IP e nomes de domínio

Endereços IP e nomes de domínio são conceitos importantes para entender ao trabalhar com a Internet.

Um endereço IP é um identificador exclusivo atribuído a cada dispositivo em uma rede. É usado para encaminhar os dados para o destino correto. Os endereços IP são normalmente representados como uma sequência de quatro números separados por pontos. Por exemplo, "192.168.1.1"

Os nomes de domínio, por outro lado, são nomes legíveis para identificar sites e outros recursos da Internet. Eles são compostos de duas ou mais partes separadas por pontos. Por exemplo, "google.com". Os nomes de domínio são traduzidos em endereço IP usando um serviço chamado Domain Name System (DNS).

Quando você insere um nome de domínio em seu navegador, seu computador envia uma consulta DNS a um servidor DNS, que retorna o endereço IP correspondente. Seu computador usa esse endereço IP para se conectar ao site ou recurso que você solicitou.

## Introdução ao HTTP e HTTPS

O Hypertext Transfer Protocol (HTTP) e o HTTP Secure (HTTPS) são protocolos de aplicação que são usados para enviar e receber dados da web.

HTTP é um protocolo usado para transferir dados entre um cliente (navegador) e um servidor (site). Quando você visita um site, seu navegador envia uma solicitação HTTP para o servidor do site. O servidor então envia uma resposta HTTP para o navegador que contém o conteúdo do site que você solicitou.

HTTPS é uma versão segura do HTTP que criptografa os dados transmitidos entre o cliente e o servidor usando criptografia SSL/TLS (Secure Sockets Layer/Transport Layer Security). Isso fornece uma camada adicional de segurança, ajudando a proteger informações confidenciais como senhas e dados de cartão de crédito.

## Construindo Aplicações com TCP/IP

TCP/IP (Transmission Control Protocol/Internet Protocol) é o protocolo de comunicação subjacente usado pela maioria das aplicações da Internet. Ele fornece uma entrega de dados confiável, ordenada e com verificação de erros entre aplicativos em diferentes dispositivos.

Ao criar aplicativos com TCP/IP, há alguns conceitos-chave a serem compreendidos:

<li> Portas: São usadas para identificar o aplicativo ou serviço em execução no dispositivo. Cada aplicativo ou serviço recebe uma porta exclusiva, permitindo que os dados sejam enviados ao destino correto. </li>
<li> Sockets: É uma combinação de um endereço IP e um número de porta, representando um endpoint específico para comunicação. Os soquetes estabelecem conexões entre dispositivos e trasferem dados entre aplicativos. </li>
<li> Conexões: São estabelecidas entre dois soquetes quando dois dispotivos desejam se comunicar entre si. Durante o processo, os dispositivos trocam informações sobre suas capacidades e recursos. </li>
<li> Transmissão de dados: Uma vez estabelecida a conexão, os dispositivos podem começar a enviar e receber dados que são transmitidos em segmentos. </li>

Ao criar aplicativos com TCP/IP, você precisará garantir que seu aplicativo seja projetado para funcionar com as portas, soquetes e conexões necessárias para a comunicação.

## Protegendo a comunicação com SSL/TLS

O SSL/TLS é usado para fornecer conexões seguras para aplicativos como navegadores da Web, clientes de e-mail e programas de transferência de arquivos.

Ao usar SSL/TLS para proteger a comunicação na internet há alguns conceitos-chaves a serem compreendidos:

<li> Certificados: São arquivos digitais que contêm informações sobre a identidade de um site ou serviço. Eles são usados para garantir que os dados enviados pela internet sejam criptografados. </li>
<li> Handshake: É um processo de negociação que é usado para estabelecer uma conexão segura entre um cliente e um servidor. </li>
<li> Cripografia: É o processo de codificação de dados para torná-los ilegíveis para pessoas não autorizadas. </li>

É importante entender como o SSL/TLS funciona e garantir que seu aplicativo seja projetado para usar SSL/TLS ao transmitir dados confidenciais, como credenciais de login, informações de pagamento e outros dados pessoais. Também é importante obter e manter certificados SSL/TLS válidos para garantir que os dados sejam criptografados corretamente.

<br>
###### Referências
Fonte: <https://cs.fyi/guide/how-does-internet-work>

