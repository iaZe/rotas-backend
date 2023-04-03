# Tudo que você precisa saber sobre DNS

## O que é DNS?

O Domain Name System (DNS) é a lista telefônica da internet. O DNS converte os nomes de domínio ("google.com") em endereços IP ("216.58.210.142") para que os navegadores possam carregar os recursos da web.

<p align="center">
  <img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/5exJlPlwAT2kQCITQhrIi9/1f771294e218b64c0490e83968075766/what_is_dns.png" width="400px"  align="center">
</p>

## Como funciona o DNS?

Mas como o DNS sabe onde encontrar o endereço IP de um determinado domínio? Ele não sabe. Ele depende de uma rede de servidores chamados DNS resolvers que trabalham juntos para encontrar nomes de domínio em endereços IP.

```
Um DNS resolver é um servidor que armazena registros de DNS e responde a consultas de DNS.
```

Quando você digita um nome de domínio em seu navegador, seu computador primeiro verifica seu cache local para ver se ele já tem o endereço IP. Se não, ele envia uma consulta ao DNS resolver mais próximo, que verificará seu próprio cache para ver se tem a resposta. Se não, ele perguntará ao DNS resolver mais próximo, e assim por diante, até que a resposta seja encontrada ou a consulta expire.

<p align="center">
<img src="../img/404.png" height="200px">
</p>

Vamos a um exemplo. Digamos que você queira visitar exemplo.com. aqui está a lista de locais envolvido na consulta DNS:

<li> Caches locais são verificados </li>
<li> Servidores DNS recursirvos são verificados </li>
<li> Servidores DNS raiz são verificados </li>
<li> Servidores DNS de domínio de nível superior (Top Level Domain) são verificados </li>
<li> Servidores DNS de autoridade de domínio são verificados </li>

<br>

<img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/3NOmAzkfPG8FTA8zLc7Li8/8efda230b212c0de2d3bbcb408507b1e/dns_record_request_sequence_recursive_resolver.png">

### Etapa 1: Caches locais

O primeiro local a ser verificado é o cache local. Esta é uma lista de nomes de domínio e seus endereços IP que seu computador acessou recentemente. Se o nome de domínio que você está procurando estiver no cache local, o endereço IP será retornado e a consulta será concluída.

Aqui está a lista de caches locais:

<li> Cache de navegador: você pode ter visitado o site antes e seu navegador pode ter armazenado em cache o endereço IP. </li>
<li> Cache DNS: Com base no TTL (Tempo de vida) do registro, seu computador pode ter armazenado em cache o endereço IP. </li>
<li> Arquivo hosts: você pode ter adicionado o endereço IP do site ao arquivo hosts do seu computador. </li>

### Etapa 2: Servidores DNS recursivos

As configurações de DNS definidas em seu computador ou roteador apontarão para um servidor DNS (por padrão é o servidor DNS do seu ISP). Este servidor pe chamado de servidor recursivo. Ele verficará seu próprio cache para ver se tem a resposta. Se isso acontecer, ele enviará a resposta de volta para o seu computador. Caso contrário, ele enviará a consulta para o próximo servidor DNS na cadeia, que é o servidor [DNS raiz](#etapa-3-servidores-dns-raiz).

### Etapa 3: Servidores DNS raiz

Os servidores DNS raiz são os servidores DNS de nível superior na hierarquia DNS. Eles são responsáveis por delegar a responsabilidade de responder a consultas para domínios de nível superior, como `.com`, `.net` e `.org`.

Eles não têm os endereços IP dos próprios sites. Em vez disso, eles têm os endereços IP dos servidores DNS do domínio de nível superior (TLD) para cada domínio de nível superior. Por exemplo, o servidor DNS raiz `.com` é `a.gtld-servers.net`. 

Você pode ver os servidores de nomes do TLD para cada domínio de nível superior [aqui](https://www.iana.org/domains/root/servers).

### Etapa 4: Servidores DNS de domínio de nível superior

Os servidores DNS de domínio de primeiro nível são responsáveis por delegar a responsabilidade de responder a consultas para domínios de segundo nível, como `google.com` e `cloudflare.com`. 

Eles não têm os endereços IP dos próprios sites. Em vez disso, eles têm os endereços IP dos servidores DNS de autoridade de domínio para cada domínio de segundo nível (ou seja, o local onde os registros DNS reais são armazenados).

### Etapa 5: Servidores DNS de autoridade de domínio

Esse é o local onde os registros DNS reais são armazenados. Nessa etapa, o servidor DNS de autoridade de domínio será consultado para o registro A do nome de domínio. O registro A é o registro DNS que mapeia um nome de domínio para um endereço IP. O servidor DNS de autoridade enviará o endereço IP de volta ao servidor DNS recursivo, que o enviará de volta ao seu computador.

<img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/1NzaAqpEFGjqTZPAS02oNv/bf7b3f305d9c35bde5c5b93a519ba6d5/what_is_a_dns_server_dns_lookup.png">

## Como funciona o DNS na prática?

Para ver como o DNS funciona na prática usamos o comando `dig`. O `dig` é uma ferramenta de linha de comando para consultar servidores de nomes DNS. Está disponível na maioria dos sistemas Linux e MacOS. Você pode instalá-lo no Windows usando o [Chocolatey](https://chocolatey.org/).

### Instalando o dig no Windows

Para instalar o dig no Windows, abra o PowerShell como administrador e execute o seguinte comando:

```
choco install dig
```

### Consultando um servidor DNS

Digamos que você queira consultar o servidor DNS do Google. Você pode fazer isso executando o seguinte comando:

```
dig +short google.com
```

O `+short` é usado para exibir apenas o endereço IP, logo teremos uma saída como:

```
216.58.210.142
```

Esse é o endereço IP para `www.google.com`. 

Caso queira aprender mais sobre o dig, você pode ler o [guia do dig](https://linux.die.net/man/1/dig).

### Como liberar o cache DNS

As vezes ser necessário liberar o cache DNS em sua máquina local. Você pode usar o comando `ipconfig` para fazer isso no Windows e o comando `dscacheutil` no MacOS.

No Windows, execute o seguinte comando:

```
ipconfig /flushdns
```

No MacOS, execute o seguinte comando:
```
dscacheutil -flushcache
```

## Conclusão

O DNS é um protocolo de rede que faz a busca dentro dos resolvers e retorna o endereço IP do site que você está procurando. 

<br>

[Anterior: Internet](/Internet.md) | [Próximo: O que é HTTP](/Internet/HTTP.md)

<br>

## Referências

* [cs.fyi](https://cs.fyi/guide/everything-you-need-to-know-about-dns)
* [Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
* [Designs.ai](https://designs.ai/)


