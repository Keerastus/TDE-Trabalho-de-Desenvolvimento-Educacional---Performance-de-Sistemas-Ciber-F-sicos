Relatório-

O código recebe 5 filósofos e 5 garfos para esse problema, cada filósofo começa o código no estado “pensando” e depois de um período de tempo muda seu estado para “com fome”, com isso pega um garfo e seguram ele até conseguirem o segundo, quando pegam o segundo mudam seu estado para “comendo”, caso o garfo esteja em posse de outro filósofo ele aguarda a liberação. Ao final solta ambos os garfos e volta para o estado de “pensando”.

Na versão i, o código apresenta um problema, os filósofos quando entram no estado de “com fome” começam pegando o garfo à sua esquerda e o seguram esse até conseguirem o da direita. Mas assim, não resta nenhum para o ciclo continuar, já que, todos já estão na posse de um filósofo, causando um deadlock. Caracterizando como a condição de espera circular de Coffman.

E na versão ii, esse problema foi resolvido quebrando essa condição. Isso foi possível, já que, ao invés deles pegarem o garfo sempre a sua esquerda primeiro, agora eles pegam o com menor id e depois o de maior, isso faz com que não haja um ciclo de espera e o deadlock não ocorre.

Fluxograma-
