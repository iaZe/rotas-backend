# Interface de sistema operacional portátil

## O que é POSIX?

POSIX (portable operating system interface) é uma família de padrões para manter a compatibilidade entre sistemas operacionais. ele descreve utilitários, APIs e serviços que um sistema operacional compatível deve fornecer ao software, facilitando assim a portabilidade de programas de um sistema para outro.

Um exemplo prático: em um sistema operacional do tipo unix, existem três fluxos padrão, stdin, stdout e stderr - são conexões de i/o que você provavelmente encontrará ao usar um terminal, pois gerenciam o fluxo da entrada padrão (stdin), saída padrão (stdout) e erro padrão (stderr).

Então, nesse caso, quando queremos interagir com algum desses streams (através de um processo, por exemplo), a api do sistema operacional POSIX facilita - por exemplo, no cabeçalho <unistd.h> c onde o stdin, stderr e stdout são definidos como stdin_fileno, stderr_fileno e stdout_fileno.

POSIX também adiciona um padrão para códigos de saída, semântica de sistema de arquivos e várias outras convenções de API de utilitário de linha de comando.

<br>

[Anterior: Introdução a sistemas operacionais](Sistemas_operacionais.md) | [Próximo: Uso do Terminal](Terminal.md)

<br>

## Referências

- [POSIX](https://pt.wikipedia.org/wiki/POSIX)
