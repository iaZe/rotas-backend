# Comunicação entre Processor (IPC)

## O que é um processo

Um processo pode ser de dois tipos:

- Processo independente
- Processo cooperativo

Um processo independente não é afetado pela execução de outros processos, enquanto um processo cooperativo pode ser afetado por outros processo em execução. Embora se possa pensar que esses processos, que estão sendo executados de forma independente, serão executados com muita eficiência, na realidade, há muitas situações em que a cooperativa pode ser utilizada para aumentar a velocidade computacional, conveniência e modularidade. A comunicação entre processos (Interprocess Communication - IPC) é um mecanismo que permite que os processos cooperem entre si e sincronizem suas ações. A comunicação entre esses processos pode ser vista como um método de cooperação entre eles. Os processos podem se comunicar uns com os outros através de:

- Memória compartilhada
- Passagem de mensagem

<p align="center">
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/1-76.png" alt="Comunicação entre processos" />
</p>

Essa é uma estrutura básica de comunicação entre processos via memória compartilhada e via método de passagem de mensagens.

Um sistema operacional pode implementar ambos os métodos de comunicação. A comunicação entre processos que usa memória compartilhada equer que os processos compartilhem alguma variável e depende completamente de como será implementada. Uma forma de comunicação usando memória compartilhada pode ser imaginada da seguinte forte

```Supondo que o processo 1 e o processo 2 estejam executando simultanemante. O processo 1 escreve em uma variável compartilhada e o processo 2 lê essa variável.```

i) Método de Memória Compartilhada:

Existem dois processos: Produtor e Consumidor. Os dois processos compartilham um espaço em comum ou local de memória conhecido como buffer, onde o item produzido pelo produtor é armazenado e do qual o consumidor lê. O produtor e o consumidor compartilharão alguma memória comum, então o produtor começará a produzir itens. Se o total de item produzido for igual ao tamanho do buffer, o produtor esperará para que seja consumido pelo consumidor. Da mesma forma, o consumidor verificará primeiro a disponibilidade do item.

#### demonstração em C

##### Dados compartilhados
```c
#define buff_max 25
#define mod %

    struct item {
 
    }
    int free_index = 0;
    int full_index = 0;
```

##### Código do Produtor
```c
item nextProduced;
    while(1){
        while(((free_index + 1) mod buff_max) == full_index);
        buffer[free_index] = nextProduced;
        free_index = (free_index + 1) mod buff_max;
    }
```

##### Código do Consumidor
```c
item nextConsumed;
    while(1){
        while(free_index == full_index);
        nextConsumed = buffer[full_index];
        full_index = (full_index + 1) mod buff_max;
    }
```

No código acima, o Produtor começará a produzir novamente quando o mod buff max estiver livre (free_index + 1), porque se não estiver livre, isso implica que ainda existem itens que podem ser consumidos, portanto, não há necessidade de produzir mais. Da mesma forma, se o ínice livre e o índice completo apontarem para o mesmo índice, isso implica que não há itens para consumir.

ii) Método de Passagem de Mensagem:

Nesse método, os processos se comunicam entre si sem usar nenhum tipo de memória compartilhada. Se dois processos p1 e p2 desejam se comunicar, eles procedem da seguinte forma:

- Estabelece um link de comunicação
- Começa a troca de mensagens

<p align="center">
  <img src="https://media.geeksforgeeks.org/wp-content/uploads/2-50.png" alt="Comunicação entre processos" />
</p>

O tamanho da mensagem pode ser fixo ou variável. Se for de tamanho fixo, é fácil para um designer de sistema operacional, mas complicado para um programador e, se for de tamanho variável, é fácil para um programador, mas complicado para o designer de sistema operacional. Uma mensagem padrão pode ter duas partes: cabeçalho e corpo.

A parte do cabeçalho é usada para armazenar o tipo de mensagem, id de destino, id de origem, tamanho da mensagem e informações de controle. As informações de controle contêm informações como o que fazer se ficar sem espaço no buffer, número de sequência, prioridade. Geralmente, a mensagem é enviada usando o estilo FIFO.

### Como os links são estabelecidos?

Um link tem alguma capacidade de determinar o número de mensagens que podem residir nele temporariamente para o qual cada link tem uma fila associada a ele que pode ser de capacidade zero, capacidade limitada ou capacidade ilimitada. Na capacidade zero, o remetente espera até que o destinatário informe ao remetente que recebeu a mensagem. Em casos de capacidade diferente de zero, um processo não sabe se uma mensagem foi recebida ou não após a operação de envio. Para isso, o remetente deve se comunicar explicitamente com o destinatário. A implementação do link depende da situação, pode ser um link de comunicação direta ou indireta.

- Links de Comunicação Direta são implementados quando os processos usam um identificador de processo específico para a comunicação, mas é difícil identificar o remetente antecipadamente. Exemplo, o servidor de impressão.

- A comunicação Indireta é feita por meio de uma caixa de correio (porta) compartilhada, que consiste em uma fila de mensagens. O remetente mantém a mensagem na caixa de correio e o destinatário pega.

### Passagem de mensagens síncrona e assíncrona:

Um processo bloqueado é aquele que está aguardando algum evento, como a disponibilização de um recurso ou a conclusão de uma operação de E/S. O IPC é possível entre os processos no mesmo computador, bem como nos processos executados em computadores diferentes, ou seja, no sistema distribuído em rede. Em ambos os casos, o processo pode não ser bloqueado durante o envio de uma mensagem ou tentativa de recebimento de uma mensagem, de modo que a passagem de mensagens pode ser bloqueada ou não. O bloqueio é considerado síncrono e o bloqueio de envio significa que o remetente será bloqueado até que a mensagem seja recebida pelo destinatário. Da mesma forma, bloquear recebimento faz com que o receptor bloqueie até que uma mensagem esteja disponível. O não bloqueio é considerado envio assíncrono e sem bloqueio faz com que o remetente envie a mensagem e continue. Da mesma forma, o recebimento sem bloqueio faz com que o destinatário receba uma mensagem válida ou nula. Existem basicamente três combinações preferidas:

- Bloqueio de envio e bloqueio de recebimento
- Envio sem bloqueio e recebimento sem bloqueio
- Envio sem bloqueio e recebimento com bloqueio (mais usado)

### Exemplos de sistema IPC

- Posix: usa o método de memória compartilhada.
- Mach: usa o método de passagem de mensagem.
- Windows XP: usa o método de passagem de mensagem usando chamadas processuais locais.

### Comunicação na arquitetura cliente-servidor

- Pipe
- Soquete
- RPC (Chamada de procedimento remoto)

### Vantagens do IPC:

- Permite que os processos se comuniquem e sincronizem entre si, levando a maior eficiência.
- Facilita a coordenação entre varios processos, levando a um melhor desempenho.
- Permite a criação de sistemas distribuídos que podem abranger vários computadores ou redes.
- Pode ser usado para implementar vários protocolos de sincronização e comunicação, como semaforos, pipes e sockets.

### Desvantagens do IPC:

- Aumenta a complexidade do sistema, tornando mais difícil de projetar e implementar.
- Pode introduzir vulnerabilidades de segurança, pois os processos podem acessar ou modificar a memória uns dos outros.
- Requer gerenciamento cuidadoso dos recursos do sistema, como memória e tempo de CPU.



<br>

[Anterior: Gerenciamento de Memória](/Sistemas_operacionais/Conhecimentos_de_Sistemas_Operacionais/Gerenciamento_de_memoria.md) | [Próximo: Gerenciamento de I/O](/Sistemas_operacionais/Conhecimentos_de_Sistemas_Operacionais/Gerenciamento_de_I_O.md)

<br>

## Referências

* [Geeks for Geeks](https://www.geeksforgeeks.org/inter-process-communication-ipc/)