# Gerenciamento de memória no OS

## O que é memória?	

A memória é um dispositivo que armazena dados e instruções para serem processados pelo processador. A memória é dividida em células de memória, cada uma com um endereço único. O processador acessa a memória por meio de um barramento de endereço, que é um conjunto de fios que transmitem o endereço da célula de memória que está sendo lida ou gravada.

## O que é memória principal?

A memória principal é a memória de acesso aleatório (RAM) que o sistema operacional e outros programas usam para armazenar dados e instruções. Algumas de suas características são sua volatilidade e sua capacidade de ser lida e gravada. Ser volátil significa que, quando a energia é desligada, o conteúdo da memória principal é perdido. Ela é usada para armazenar dados e instruções que são usados ​​com frequência sendo muito mais rápida que o armazenamento secundário, como discos rígidos e unidades de estado sólido.

<p align="center">
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20221116104505/1white-660x453.png" height="250px">
</p>

## O que é o Gerencia de Memória?

Em um computador de multiprogramação, o sistema operacional reside em uma parte da memória e o restante é usado por vários processos. A tarefa de subdividir a memória entre diferentes processos é chamada de Gerenciamento de Memória. Sendo ele um método no sistema operacional para gerenciar as operações entre a memória principal e o disco durante a execução do processo.

### Porque o gerenciamento de memória é necessário?

- Alocar e desalocar a memória quando necessário.
- Para acompanhar o espaço de memória usada por processos.
- Para minimizar problemas de fragmentação.
- Para a utilização adequada da memória. 
- Para manter a integridade dos dados durante a execução dos processos.

## Espaços de endereço Lógico e Físico

- **Espaço de endereço lógico**: Um endereço gerado pela CPU é conhecido como `endereço lógico`. Também pode ser chamado de `endereço virtual`. O espaço de endereço lógico pode ser definido como o tamanho do processo. Um endereço lógico pode ser alterado.

- **Espaço de endereço físico**: Um endereço gerado pela unidade de gerenciamento de memória é conhecido como `endereço físico`. Também pode ser chamado de `endereço real`. O espaço de endereço físico pode ser definido como o tamanho da memória principal. O mapeamento de tempo de execução de endereços virtuais para físico é feito por um dispositivo de hardware chamado de Memory Management Unit (MMU).Um endereço físico nunca é alterado.

## Carregamento Estático e Dinâmico (Loading)

O carregamento de um processo na memória principal é feito por um carregador. Existem dois tipos diferentes de carregamento:

- **Carregamento estático**: Carregamento estático é basicamente carregar todo o programa em um endereço fixo. Requer mais espaço de memória.

- **Carregamento dinâmico**: Todo programa e todos os dados de um processo devem estar na memória física para que o processo seja executado. Assim, o tamanho de um processo é limitado ao tamanho da memória física.

## Link Estático e Dinâmico (Linking)

Um vinculador é um programa que pega um ou mais arquivos gerados por um compilador e os combina em um único arquivo executável. Existem dois tipos diferentes de vinculação:

- **Vinculação estática**: Na vinculação estática, o vinculador combina todos os módulos de programa necessários em um único programa executável. Portanto não há dependência de tempo de execução.

- **Vinculação dinâmica**: O conceito de vinculação dinâmica é semelhante ao carregamento dinâmico. Na vinculação dinâmica, "Stub" é incluído para cada referência de rotina na biblioteca apropriada. Um stub é um pequeno pedaço de código. Quando o stub é executado, ele verifica se a rotina necessária já está na memória ou não. Se não estiver disponível, o programa carrega a rotina na memória.

## Swapping

Quando um processo é executado, ele deve residir na memória. O swapping é um processo de trocar um processo temporiariamente em uma memória secundária da memória principal, que é rápido em comparação com a memória principal. Uma troca permite que mais processos sejam executados e pode caber na memória de uma só vez. A parte principal da troca é o tempo de transferência e o tempo total é diretamente proporcional à quantidade de memória trocada.

<p align="center">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20221116104533/2white-660x441.png" height="250px">
</p>

### Gerenciamento de memória com monoprogramação (sem swapping)

Esta é a abordagem de gerenciamento de memória mais simples, a memória é dividida em duas partes:

- Uma parte do sistema operacional
- Uma parte para o programa do usuário

Nessa abordagem, o sistema operacional rastreia o primeiro e o último local disponível para a alocação do programa do usuário.

## Alocação de Memória Contígua

A memória principal deve atender tanto o sistema operacional quanto os diferentes processos clientes. Portanto, a alocação de memória torna-se uma tarefa importante no sistema operacional. A memória geralmente é dividida em duas partições: uma para o sistema operacional e outra para os processos do usuário.

<p align="center">
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20221116104926/3white.png" height="250px">
</p>

## Alocação de memória

Para obter a utilização adequada da memória, a alocação de memória deve ser alocada de maneira eficiente. Um dos métodos mais simples para alocar memória é dividir a memória em várias partições de tamanho fixo e cada partição contém exatamente um processo. Assim, o grau de multiprogramação é obtido pelo número de partições.

- **Alocação de várias partições**: Nesse método, um processo é selecionado da fila de entrada e carregado na partição livre. Quando o processo termina, a partição fica disponível para outros processos.

- **Alocação de partição fixa**: Nesse método, o sistema operacional mantém uma tabela que inidica quais partes da memória estão disponíveis e quais estão ocupadas por processos. Inicialmente, toda a memória está disponível para os processos do usuário e é considerada um grande bloco de memória disponível.

## Fragmentação

A fragmentação é definida quando o processo é carregado e removido após a execução da memória, criando um pequeno buraco livre. Esses furos não podem ser atribuídos a novos processos porque os furos não são combinados ou não atendem ao rquisito de memória do processo. Para atingir um grau de multiprogramação mais alto, devemos reduzir o desperdício de memória ou problemas de fragmentação.

## Paginação

A paginação é um esquema de gerenciamento de memória que elimina a necessidade de uma alocação contígua de memória física. Esse esquema permite que o espaço de endereço físico de um processo seja não contíguo.

- **Endereço Lógico (representado em bits)**: O endereço gerado pelo CPU.
- **Espaço de Endereço Lógico (representado em bytes)**: O conjunto de todos os endereços lógicos gerados por um programa.
- **Endereço Físico (representado em bits)**: O endereço disponível em uma unidade de memória
- **Espaço de Endereço Físico(representado em bytes)**: O conjunto de todos os endereços físicos correspondentes aos endereços lógicos.

**Exemplo**:

- Se o endereço lógico for de 32 bits, o espaço de endereço lógico será de 2 ^ 32 bytes.
- Se o espaço de endereço lógico for de 128 M palavras, o endereço lógico será de 27 bits.
- Se o endereço físico for 22 bits, o espaço de endereço físico será de 2 ^ 22 bytes.

O mapeamento do endereço virtual para o físico é feito pela unidade de gerenciamento de memória (MMU).

- O espaço de enderaçamento físico é conceitualmente dividido em vários blocos de tamanho fixo, chamados quadros.
- O espaço de endereçamento lógico também é divido em blocos de tamanho fixo, chamados de páginas.
- Tamanho da página = tamanho do quadro

Considerando um exemplo:

- Endereço físico tem 12 bits, então o Espaço de endereço físico tem 2 ^ 12 = 4096 bytes.
- Endereço lógico tem 13 bits, então o Espaço de endereço lógico tem 2 ^ 13 = 8192 bytes.


<br>

[Anterior: Como os sistemas operacionais funcionam](/Sistemas_operacionais/Conhecimentos_de_Sistemas_Operacionais/Como_os_sistemas_operacionais_funcionam.md) | [Próximo: Comunicação entre processos](/Sistemas_operacionais/Conhecimentos_de_Sistemas_Operacionais/Comunicacao_entre_processos.md)

<br>

## Referências

* [Geeks For Geeks](https://www.geeksforgeeks.org/memory-management-in-operating-system/)
