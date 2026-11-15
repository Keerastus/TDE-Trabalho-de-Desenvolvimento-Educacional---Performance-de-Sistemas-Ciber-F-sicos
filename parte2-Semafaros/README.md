Parte 2 — Threads e Semáforos

Objetivo: demonstrar uma condição de corrida incrementando um contador compartilhado a
partir de múltiplas threads sem sincronização e, em seguida, corrigi-la com um semáforo
binário, comparando o valor final e o tempo de execução das duas versões.

Como executar:
No arquivo contador.py, precisa alternar entre as duas funções, comentando uma e deixando a outra ativa.

Execução sem semáforo:

Na criação da thread, deixe ativa a linha 38:

thread = threading.Thread(target=incrementar)

E mantenha comentada a linha 40:

thread = threading.Thread(target=incrementarSemaforo)

Execução com semáforo:

Na criação da thread, comentar a primeira linha e deixar ativa a segunda:

#thread = threading.Thread(target=incrementar)

thread = threading.Thread(target=incrementarSemaforo)


Discussões:

Na versão sem sincronização, todas as threads acessam e modificam a mesma variável. 
Como não existe proteção, duas threads podem interferir as mesmas operações, fazendo com que uma
atualização sobrescreva a outra, e isso pode gerar a perda de incrementos.

Na segunda versão, usando um semáforo inicializado com uma permissão, antes de incrementar o contador,
a thread precisa adquirir o semáforo, e libera-lo depois da operação.
Assim, somente uma thread por vez consegue acessar a seção crítica, o que evita conflitos na atualização
do contador e garante o resultado esperado.


Throughput
O semáforo adiciona um custo tempo, pois as threads precisam aguardar a liberação
dele. Isso pode reduzir o throughput, já que as operações não acontecem simultaneamente dentro da seção crítica,
mas, esse custo é necessário para garantir a consistência dos dados.


Visibiliade/ordenação:
Os mecanismos de sincronização são importantes para garantir que as alterações feitas por uma
thread sejam vistas corretamente pélas outras.

Em Python, os mecanismos de sincronização da biblioteca threading coordenam o acesso à memória compartilhada
e a visibilidade das alterações.


Resultados:

Esperado: 1.600.000

Sem semaforo: 1 - total= 1600000  tempo= 0.04779209999833256
              2 - total= 1600000  tempo= 0.04974640000727959
              3 - total= 1600000  tmepo= 0.049154400010593235

Com semaforo: 1 - total= 1600000  tempo= 1.0621157999848947
              2 - total= 1600000  tempo= 1.0419636000005994
              3 - total= 1600000  tmepo= 1.0685057000082452

No Python, existe o GIL (Global Interpreter Lock), que controla a execução de instruções Python entre as threads no CPython tradicional.
Por causa dele, algumas operações podem acabar sendo executadas de maneira que dificulte a ocorrência de uma condição de corrida. 
Por isso, mesmo sem utilizar um semáforo, é possível que o contador alcance o valor esperado em algumas ou até em todas as execuções.