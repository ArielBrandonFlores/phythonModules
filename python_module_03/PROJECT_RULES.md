# Python Module 03 - Data Quest: Mastering Python Collections

> Documento de referência e regras operacionais para o desenvolvimento dos exercícios do Módulo 03 de Python (Versão 3.0).

---

## 1. Diretrizes Gerais e Restrições Globais (Chapter IV)

Todas as resoluções neste módulo devem obedecer estritamente aos seguintes critérios:

* **Versão do Python:** Python 3.10 ou superior.
* **Padrão de Código:** Conformidade estrita com o linter `flake8` (PEP 8, limite de tamanho de linha, espaçamentos, imports limpos, etc.).
* **Tipagem Estática:** Todas as funções e métodos devem conter **type hints** explícitos (parâmetros e retorno). A conformidade deve ser validada via `mypy`.
* **Tratamento de Exceções:** Todos os erros e dados inesperados devem ser tratados graciosamente com blocos `try/except` para impedir que o programa quebre ou exiba tracebacks não tratados.
* **Proibição de I/O em Arquivos:** Nenhuma operação de leitura/escrita em arquivos é permitida (`open()`, etc.). Todos os dados devem ser processados em memória, via parâmetros de linha de comando (`sys.argv`) ou entrada padrão (`input()`).
* **Tipos Padrão Autorizados:** Tipos primitivos permitidos: `str`, `int`, `float`, bem como seus construtores e métodos associados.
* **Coleções e Estruturas:** O objetivo central é demonstrar o uso correto de coleções (`list`, `tuple`, `set`, `dict`), além de geradores (`yield`, `next()`) e *comprehensions*.
* **Entrega:** Devem ser submetidos apenas os arquivos requisitados dentro de seus respectivos diretórios (`ex0/`, `ex1/`, ..., `ex6/`).

---

## 2. Mapa dos Exercícios

| Exercício | Diretório | Arquivo Obrigatório | Conceito Central | Autorizados Específicos |
| :--- | :--- | :--- | :--- | :--- |
| **Ex 0: Command Quest** | `ex0/` | `ft_command_quest.py` | Argumentos CLI & Listas | `import sys`, `sys.argv`, `len()`, `print()` |
| **Ex 1: Score Cruncher** | `ex1/` | `ft_score_analytics.py` | Listas & Tratamento de Erros | `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()` |
| **Ex 2: Position Tracker** | `ex2/` | `ft_coordinate_system.py` | Tuplas & Matemática 3D | `import math`, `math.sqrt()`, `input()`, `round()`, `print()` |
| **Ex 3: Achievement Hunter** | `ex3/` | `ft_achievement_tracker.py` | Conjuntos (`set`) & Álgebra de Conjuntos | `len()`, `print()`, `import random`, `random.*`, `set()`, `set.union()`, `set.intersection()`, `set.difference()` |
| **Ex 4: Inventory Master** | `ex4/` | `ft_inventory_system.py` | Dicionários (`dict`) | `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys()`, `dict.values()`, `dict.update()` |
| **Ex 5: Stream Wizard** | `ex5/` | `ft_data_stream.py` | Geradores (`yield`, streams) | `next()`, `range()`, `len()`, `print()`, `import typing`, `typing.Generator`, `import random`, `random.*` |
| **Ex 6: Data Alchemist** | `ex6/` | `ft_data_alchemist.py` | List & Dict Comprehensions | `import random`, `random.*`, `print()`, `len()`, `sum()`, `round()` |

---

## 3. Especificação Detalhada por Exercício

### Exercise 0: Command Quest (`ex0/ft_command_quest.py`)
* **Objetivo:** Manipular a lista nativa `sys.argv`.
* **Funções/Módulos Permitidos:** `import sys`, `sys.argv`, `len()`, `print()`.
* **Regras de Comportamento:**
  * Exibir cabeçalho: `=== Command Quest ===`.
  * Exibir o nome do programa: `Program name: ft_command_quest.py`.
  * Se nenhum argumento extra for passado:
    * Exibir `No arguments provided!`.
    * Exibir `Total arguments: 1` (contando o script).
  * Se argumentos forem passados:
    * Exibir `Arguments received: <N>` (quantidade excluindo o script).
    * Listar cada argumento no formato: `Argument <i>: <valor>`.
    * Exibir `Total arguments: <total>` (quantidade total de `sys.argv`).

---

### Exercise 1: Score Cruncher (`ex1/ft_score_analytics.py`)
* **Objetivo:** Processar argumentos de pontuação, filtrar entradas inválidas e gerar estatísticas básicas usando listas.
* **Funções/Módulos Permitidos:** `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()`.
* **Regras de Comportamento:**
  * Exibir cabeçalho: `=== Player Score Analytics ===`.
  * Para cada argumento não numérico (falha na conversão para número/int):
    * Exibir: `Invalid parameter: '<param>'` e descartá-lo.
  * Se nenhum argumento for passado ou nenhum valor válido restar:
    * Exibir: `No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...`.
  * Caso haja valores válidos:
    * Guardar pontuações em uma lista.
    * `Scores processed: [<val1>, <val2>, ...]`.
    * `Total players: <qtd>`.
    * `Total score: <soma>`.
    * `Average score: <media>` (float).
    * `High score: <max>`.
    * `Low score: <min>`.
    * `Score range: <max - min>`.

---

### Exercise 2: Position Tracker (`ex2/ft_coordinate_system.py`)
* **Objetivo:** Utilizar tuplas imutáveis para armazenar e calcular posições 3D `(x, y, z)`.
* **Funções/Módulos Permitidos:** `import math`, `math.sqrt()`, `input()`, `round()`, `print()`.
* **Regras de Comportamento:**
  * Função obrigatória: `get_player_pos() -> tuple[float, float, float]`:
    * Solicita coordenadas no formato `'x,y,z'`.
    * Trata entradas inválidas (número de parâmetros != 3 ou erro de conversão para float).
    * Mensagem de erro de sintaxe (ex: não tem 3 campos): `Invalid syntax`.
    * Mensagem de erro de valor: `Error on parameter '<p>': could not convert string to float: '<p>'`.
    * Repete a solicitação até obter uma entrada válida.
    * Retorna a tupla `(x, y, z)`.
  * Fluxo principal:
    * Obter 1º conjunto de coordenadas.
    * Exibir tupla: `Got a first tuple: (x, y, z)`.
    * Exibir coordenadas individualmente: `It includes: X=<x>, Y=<y>, Z=<z>`.
    * Calcular distância euclidiana até a origem `(0, 0, 0)`:
      $$\text{distância} = \sqrt{x^2 + y^2 + z^2}$$
    * Exibir `Distance to center: <distancia arredondada para 4 casas decimais>`.
    * Obter 2º conjunto de coordenadas via `get_player_pos()`.
    * Calcular e exibir distância euclidiana entre o 2º e o 1º ponto:
      $$\text{distância} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
    * Exibir: `Distance between the 2 sets of coordinates: <distancia arredondada para 4 casas decimais>`.

---

### Exercise 3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)
* **Objetivo:** Utilizar conjuntos (`set`) e operações de álgebra booleana de conjuntos (união, interseção, diferença).
* **Funções/Módulos Permitidos:** `len()`, `print()`, `import random`, `random.*`, `set()`, `set.union()`, `set.intersection()`, `set.difference()`.
* **Regras de Comportamento:**
  * Função obrigatória: `gen_player_achievements() -> set[str]`:
    * Utiliza uma lista fixa e ampla de conquistas predefinidas.
    * Escolhe aleatoriamente uma quantidade de conquistas e as sorteia da lista para formar um `set`.
  * Gerar conjuntos para no mínimo 4 jogadores (Alice, Bob, Charlie, Dylan).
  * Exibir as conquistas de cada jogador.
  * Calcular e exibir:
    * Conquistas distintas totais entre todos os jogadores (União).
    * Conquistas compartilhadas por todos os jogadores (Interseção).
    * Para cada jogador: conquistas que só ele possui (Diferença em relação à união dos demais).
    * Para cada jogador: conquistas ausentes que ele precisa para ter todas (Diferença entre o total do universo e o seu conjunto).

---

### Exercise 4: Inventory Master (`ex4/ft_inventory_system.py`)
* **Objetivo:** Gerenciar o inventário de um jogo usando dicionários (`dict`).
* **Funções/Módulos Permitidos:** `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys()`, `dict.values()`, `dict.update()`.
* **Regras de Comportamento:**
  * Receber argumentos no formato `<item_name>:<quantity>`.
  * Validação com descarte e mensagens de erro:
    * Itens repetidos: `Redundant item '<nome>' - discarding`.
    * Sintaxe inválida (sem `:`): `Error - invalid parameter '<param>'`.
    * Quantidade inválida: `Quantity error for '<chave>': invalid literal for int() with base 10: '<valor>'`.
  * Armazenar as quantidades como inteiros no dicionário.
  * Operações a exibir:
    * Dicionário completo: `Got inventory: { ... }`.
    * Lista de itens: `Item list: [ ... ]`.
    * Quantidade total: `Total quantity of the <N> items: <total>`.
    * Porcentagem de cada item no inventário total: `Item <nome> represents <pct>%` (arredondado em 1 casa decimal).
    * Item mais e menos abundante: `Item most abundant: <nome> with quantity <qtd>` / `Item least abundant: ...` (em caso de empate, priorizar o que apareceu primeiro na linha de comando).
    * Inserir um novo item e exibir inventário atualizado (`Updated inventory: ...`).

---

### Exercise 5: Stream Wizard (`ex5/ft_data_stream.py`)
* **Objetivo:** Criação e consumo de geradores com `yield` para economia de memória e processamento sob demanda.
* **Funções/Módulos Permitidos:** `next()`, `range()`, `len()`, `print()`, `import typing`, `typing.Generator`, `import random`, `random.*`.
* **Regras de Comportamento:**
  * Gerador infinito `gen_event() -> Generator[tuple[str, str], None, None]`:
    * Sorteia um nome de jogador e uma ação de listas fixas.
    * Produz indefinidamente tuplas `(name, action)`.
  * No fluxo principal:
    * Iterar 1.000 vezes consumindo eventos do gerador com `next()` e exibindo cada um: `Event <i>: Player <name> did action <action>`.
    * Criar uma lista de 10 tuplas geradas por `gen_event()`.
    * Exibir a lista gerada: `Built list of 10 events: [ ... ]`.
  * Gerador consumidor `consume_event(events_list: list) -> Generator[tuple[str, str], None, None]`:
    * A cada iteração, sorteia aleatoriamente um elemento da lista, remove-o (`list.pop` ou similar) e o produz com `yield`, até que a lista esteja vazia.
    * Deve ser consumido diretamente na sintaxe `for ... in ...`.
    * A cada iteração do loop, exibir o evento consumido e o que restou na lista.

---

### Exercise 6: Data Alchemist (`ex6/ft_data_alchemist.py`)
* **Objetivo:** Manipulação avançada e concisa usando *List Comprehensions* e *Dict Comprehensions*.
* **Funções/Módulos Permitidos:** `import random`, `random.*`, `print()`, `len()`, `sum()`, `round()`.
* **Regras de Comportamento:**
  * Lista inicial de nomes com capitalização mista (alguns maiúsculos/capitalizados, outros minúsculos).
  * Criar duas *List Comprehensions*:
    1. Lista com todos os nomes capitalizados (`capitalize()` / `title()`).
    2. Lista filtrando apenas os nomes que já estavam capitalizados na lista original.
  * Criar duas *Dict Comprehensions*:
    1. Dicionário mapeando a lista de nomes capitalizados para pontuações aleatórias.
    2. Dicionário filtrando apenas os jogadores com pontuação estritamente superior à média (`score > average`).
  * Regra estilística obrigatória: cada *comprehension* deve ocupar preferencialmente uma única linha (a não ser que exceda o limite de caracteres do linter).

---

## 4. Checklist de Qualidade e Conformidade para Avaliação

Antes de finalizar qualquer exercício:
1. [ ] **Flake8:** Executar `flake8` no arquivo e certificar zero avisos/erros.
2. [ ] **Mypy:** Executar `mypy --strict` ou checagem estrita de tipos sem erros.
3. [ ] **Funções Autorizadas:** Não importar nem usar funções além das explicitamente autorizadas em cada exercício.
4. [ ] **Tratamento de Exceções:** Testar entradas vazias, dados inválidos e formatos errados sem crash.
5. [ ] **Saída Idêntica ao Enunciado:** Assegurar que os textos, formatações e mensagens de saída correspondam exatamente aos exemplos fornecidos no subject.

