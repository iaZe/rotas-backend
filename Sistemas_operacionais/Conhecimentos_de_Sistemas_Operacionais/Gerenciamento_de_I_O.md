# Gerenciamento de Entradas e Saídas (Input and Output)

## Entrada e Saída

Uma das tarefas importantes de um sistema operacional é gerenciar vários dispositivos de E/S, incluindo mouse, teclado, dispositivos USB.
Um sistema de E/S é necessário para receber uma solicitação de E/S de um aplicativo e enviá-la ao dispositivo físico, em seguida, receber qualquer resposta do dispositivo e enviá-la de volta ao aplicativo. Os dispositivos de E/S podem ser divididos em duas categorias:

- **Dispositivo de bloco**: Um dispositivo de bloco é aquele com qual o drive se comunica enviando blocos inteiros de dados. Por exemplo, disco rígido, CD-ROM, etc.
- **Dispositivo de caractere**: Um dispositivo de caractere é aquele com qual o drive se comunica enviando um caractere por vez (bytes, octetos). Por exemplo, teclado, mouse, impressora, etc.

## Controladores de dispositivos

Os drivers de dispositivo são módulos de software que podem ser conectados a um sistema operacional para lidar com um dispositivo específico. O sistema operacional recebe ajuda dos drivers de dispositivos para lidar com todos os dispositivos de E/S.

O Device Controller funciona como uma interface entre um dispositivo e um driver de dispositivo. As unidades de E/S (teclado, mouse, impressora, etc.) geralmente consistem em um componente mecânico e um componente eletrônico, onde o componente eletrônico é chamado de controlador do dispositivo.

Há Sempre um controlador de dispositivo e um driver de dispositivo para cada dispositivo se comunicar com os sistemas operacionais. Um controlador de dispositivo pode ser capaz de lidar com vários dispositivos. Como uma interface, sua principal tarefa é converter o fluxo de bits serial em bloco de bytes, executar a correção de erros conforme necessário.

Qualquer dispositivo conectado ao computador é conectado por um plugue e soquete, e o soquete é conectado a um controlador de dispositivo. A seguir está um modelo para conectar a CPU, memória, controladores e dispositivos de E/S onde a CPU e os controladores de dispositivos usam um barramento comum para comunicação.

<p align="center">
  <img src="https://www.tutorialspoint.com/operating_system/images/device_controllers.jpg" alt="Controladores de dispositivos"  height="250px">
</p>

## Entra e Saida síncrona e assíncrona

- **E/S Sincrona**: A executção da CPU espera enquanto a E/S é executada.
- **E/S Assíncrona**: A execução da CPU não espera enquanto a E/S é executada.

## Comunicação para dispositivos de E/S

A CPU deve ter uma maneira de passar informações de e para um dispositivo de E/S. Existem três maneiras de fazer isso:

- E/S de instrução especial
- E/S de mapeamento de memória
- Acesso direto à memória (DMA)

### E/S de instrução especial

Usa instruções de CPU feitas especificamente para controlar dispositivos de E/S. Essas instruções geralmente permitem que os dados sejam enviados para um dispositivo de E/S ou lidos em um dispositivo de E/S.

### E/S de mapeamento de memória

Ao usar E/S mapeada em memória, o mesmo espaço de endereço é compartilhado pela memória e pelos dispositivos de E/S. O dispositivo é conectado diretamente a determinados locais da memória principal para que o dispositivo de E/S possa transferir blocos de dados de/para a memória sem passar pela CPU

<p align="center">
  <img src="https://www.tutorialspoint.com/operating_system/images/memory_mapped_io.jpg" alt="E/S de mapeamento de memória"  height="250px">
</p>

Ao usar a E/S mapeada na memória, o sistema operacional aloca o buffer na memória e informa o dispostivo de E/S para usar esse buffer para enviar dados para a CPU. O dispositivo de E/S opera de forma assíncrona com a CPU e interrompe a CPU quando termina.

A vantagem desse método é que toda instrução que pode acessar a memória pode ser usada para manipular um dispositivo de E/S. Entrada e saída mapeada em memória é usada na maioria dos dispositivos de E/S de alta velocidade.

### Acesso direto à memória (DMA)

Dispositivos lentros como teclados irão gerar uma interrupção para a CPU principalmente após a transferência de cada byte. Se um dispositivo rápido, como um disco, gerasse uma interrupção para cada byte, o sistema operacional gastaria a maior parte do tempo lidando com essas interrupções. Portanto, um computador típico usa hardware de acesso direto à memória (Direct Memory Access - DMA) para reduzir essa sobrecarga.

Acesso direto à memória significa que a CPU concede autoridade ao módulo de E/S para ler ou gravar na memória sem envolvimento. O próprio módulo DMA controla a troca de dados entre a memória principal e o dispositivo de E/S. A CPU só está envolvida no início e no fim da transferência e é interrompida somente após a transferência do bloco inteiro.

O acesso direto à memória precisa de um hardware chamado controlador DMA (DMAC) que gerencia as transferências de dados e arbitra o acesso ao barramento do sistema. Os controladores são programados com ponteiros de origem e destino, contadores para rastrear o número de bytes transferidos e configurações, que incluem tipos de E/S e memória, interrupções e estados para os ciclos da CPU.

<p align="center">
  <img src="https://www.tutorialspoint.com/operating_system/images/dma.jpg" alt="Acesso direto à memória"  height="250px">
</p>

| **Etapa** | **Descrição** |
|-----------|---------------|
| 1         | O driver do dispositivo é instruído a transferir dados do disco para um endereço de buffer X. |
| 2         | O driver do dispositivo instrui o controlador de disco a transferir dados para o buffer. |
| 3         | O controlador de disco inicia a transferência DMA. |
| 4         | O controlador de disco envia cada byte para o controlador DMA. |
| 5         | O controlador DMA transfere bytes para o buffer, aumenta o endereço de memória, diminui o contador C até que C se torne zero. |
| 6         | Quando C torna-se zero, o DMA interrompe a CPU para sinalizar a conclusão da transferência. |

## Polling e Interrupções

Um computador deve ter uma maneira de detectar a chegada de qualquer tipo de entrada. Existem duas maneiras de isso acontecer, conhecidas como `polling` e `interrupções`. Ambas as técnicas permitem ao processador lidar com eventos que podem ocorrer a qualquer momento e que não estão relacionados ao processo que está executando no momento.

### Polling de E/S

O polling é a maneira mais simples de um dispositivo de E/S se comunicar com o processador. O processo de verificação periódica do status do dispositivo para ver se é hora da próxima operação de E/S é chamado de polling. O dispositivo de E/S simplesmente coloca as informações em um registrador de status e o processador deve vir e obter as inforamções.

Na maioria das vezes, os dispositivos não exigirão atenção e, quando o fizerem, terão que esperar até que sejam interrogados novamente pelo programa. Este é um método ineficiente e muito do tempo dos processadores é desperdiçado em pesquisas desnecessárias.


### Interrupções de E/S

Um esquema alternativo para lidar com E/S é o método orientado a interrupção. Uma interrupção é um sinal para o microprofessador de um dispositivo que requer atenção.

Um controlador de dispositivo coloca um sinal de interrupção no barramento quando precisa da atenção da CPU quando a CPU recebe uma interrupção. Ele salva seu estado atual e invoca o manipulador de interrupção apropriado usando o vetor de interrupção. Quando o dispositivo de interrupção é tratado, a CPU continua com sua tarefa original como se nunca tivesse sido interrompida.

<br>

[Anterior: Comunicação entre processos](Comunicacao_entre_processos.md) | [Próximo: Conceitos básicos de Networking](Conceitos_basicos_de_Networking.md)

<br>

## Referências

* [TutorialsPoint](https://www.tutorialspoint.com/operating_system/os_io_hardware.htm)