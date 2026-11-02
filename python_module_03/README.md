# Python Module 03 — Data Quest: Mastering Python Collections

Guia de estudos e documentação técnica completa do **Python Module 03 (Versão 3.0)**. Este documento foi estruturado especificamente para servir como material de revisão e apoio durante a defesa (avaliação entre pares), explicando a lógica, as decisões arquiteturais e o raciocínio por trás de cada exercício.

---

## 🎯 Linha de Raciocínio Unificada do Projeto

O módulo simula a construção progressiva de uma **plataforma de telemetria e análise para jogos online**:

1. **ex0 (Entrada de Dados):** O sistema precisa receber parâmetros do mundo externo via linha de comando (`sys.argv`).
2. **ex1 (Limpeza e Estatísticas):** Os dados recebidos (pontuações) precisam ser validados e agregados em listas (`list`), calculando métricas.
3. **ex2 (Geometria e Imutabilidade):** Os jogadores navegam em um mundo 3D, necessitando de coordenadas imutáveis seguras (`tuple`) e cálculo de distâncias euclidianas.
4. **ex3 (Conquistas e Unicidade):** O jogo monitora medalhas/troféus únicos dos jogadores com operações matemáticas de conjuntos (`set`).
5. **ex4 (Mapeamento de Inventário):** Itens e quantidades exigem pares chave-valor (`dict`), permitindo cálculos rápidos de estoque e porcentagens.
6. **ex5 (Processamento sob Demanda):** Milhões de ações de jogadores geram fluxos contínuos de dados sem esgotar a memória RAM usando geradores (`yield`).
7. **ex6 (Transformação Condensada):** As estruturas de dados são filtradas e transformadas de forma elegante e concisa com *comprehensions*.

---

## 📚 Detalhamento dos Exercícios

---

### Exercise 0: Command Quest (`ex0/ft_command_quest.py`)

* **Diretório:** `ex0/`
* **Arquivo:** `ft_command_quest.py`
* **Conceito:** Manipulação de listas nativas (`sys.argv`).

#### Para que serve e Descrição
Permite que o programa receba e identifique argumentos passados pelo usuário no terminal. Demonstra que a linha de comando é representada pelo Python como uma lista sequencial de strings onde o primeiro elemento (`sys.argv[0]`) é sempre o nome do próprio script.

#### O que foi aprendido
* Importação e uso do módulo padrão `sys`.
* A estrutura da lista `sys.argv` (equivalente ao `char *argv[]` em C).
* Fatiamento de listas (`sys.argv[1:]`) para separar os argumentos do nome do programa.
* Uso de `len()` para calcular o número total de argumentos.

#### Roteiro para Explicar na Defesa
> **"Por que `sys.argv[0]` não é contado como argumento recebido?"**  
> *"Porque `sys.argv[0]` representa a invocação do executável/script. O usuário do programa só forneceu os argumentos que vêm a partir do índice 1 (`sys.argv[1:]`), totalizando `len(sys.argv) - 1` entradas reais."*

---

### Exercise 1: Score Cruncher (`ex1/ft_score_analytics.py`)

* **Diretório:** `ex1/`
* **Arquivo:** `ft_score_analytics.py`
* **Conceito:** Listas mutáveis (`list`), agregação numérica e tratamento de erros (`try/except`).

#### Para que serve e Descrição
Recebe uma série de pontuações via CLI, descarta entradas corrompidas ou não numéricas sem quebrar o programa, armazena os valores válidos em uma lista e calcula métricas fundamentais: total de jogadores, soma, média, maior pontuação, menor pontuação e amplitude (*range*).

#### O que foi aprendido
* Tratamento gracioso de exceções com `try/except ValueError` para conversão de tipos.
* Construção de listas dinâmicas com o método `.append()`.
* Funções embutidas de alta performance para listas numéricas: `sum()`, `max()`, `min()`.
* Prevenção de crashes quando nenhuma pontuação válida é fornecida.

#### Roteiro para Explicar na Defesa
> **"Por que usar listas em vez de tuplas aqui?"**  
> *"Porque a lista é mutável e seu tamanho cresce dinamicamente conforme validamos cada argumento da linha de comando com `.append()`. A tupla é imutável e tem tamanho fixo."*
>
> **"Como calculamos o score range?"**  
> *"É a diferença entre o maior valor e o menor valor: `max(valid_scores) - min(valid_scores)`."*

---

### Exercise 2: Position Tracker (`ex2/ft_coordinate_system.py`)

* **Diretório:** `ex2/`
* **Arquivo:** `ft_coordinate_system.py`
* **Conceito:** Tuplas (`tuple`), imutabilidade e fórmula da distância Euclidiana 3D.

#### Para que serve e Descrição
Captura coordenadas espaciais `(x, y, z)` informadas pelo usuário, valida a sintaxe e o tipo dos dados com repetição até que uma entrada correta seja inserida, empacota os dados em uma tupla imutável e calcula a distância euclidiana tanto para a origem `(0, 0, 0)` quanto entre dois pontos distintos no espaço 3D.

#### O que foi aprendido
* Características das tuplas: imutáveis, ordenadas e indexadas.
* Desempacotamento de tuplas e acesso por índice (`pos[0]`, `pos[1]`, `pos[2]`).
* Uso do módulo `math` e da função `math.sqrt()`.
* Extensão 3D do Teorema de Pitágoras:
  $$\text{distância} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
* Arredondamento controlado de casas decimais com `round(valor, 4)`.

#### Roteiro para Explicar na Defesa
> **"Por que coordenadas devem ser tuplas e não listas?"**  
> *"Coordenadas representam um ponto estático no espaço. Como tuplas são imutáveis ('escritas em pedra'), garantem integridade referencial: nenhum método externo pode acidentalmente alterar o `x`, `y` ou `z` desse ponto após criado."*

---

### Exercise 3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)

* **Diretório:** `ex3/`
* **Arquivo:** `ft_achievement_tracker.py`
* **Conceito:** Conjuntos (`set`) e operações de teoria dos conjuntos (União, Interseção e Diferença).

#### Para que serve e Descrição
Gerencia o sistema de conquistas (*achievements*) de múltiplos jogadores, sorteando conquistas de um catálogo e aplicando álgebra de conjuntos para responder perguntas de telemetria:
1. Quais conquistas foram obtidas por ao menos um jogador? (**União**)
2. Quais conquistas todos os jogadores têm em comum? (**Interseção**)
3. Quais conquistas são exclusivas de determinado jogador? (**Diferença**)
4. Quais conquistas faltam para um jogador completar 100%? (**Diferença com o universo**)

#### O que foi aprendido
* Características de um `set`: elementos únicos (sem duplicatas), não indexados, baseados em tabela hash ($O(1)$ para busca).
* Métodos oficiais autorizados: `set.union()`, `set.intersection()`, `set.difference()`.
* Módulo `random` (`random.randint`, `random.sample`).

#### Roteiro para Explicar na Defesa
> **"Por que Python imprime um conjunto vazio como `set()` e não `{}`?"**  
> *"Porque as chaves vazias `{}` já são reservadas pelo Python para criar um dicionário vazio (`dict()`). Portanto, o Python representa um conjunto vazio como `set()` para evitar ambiguidade."*
>
> **"Qual a vantagem do `set` sobre a `list` para conquistas?"**  
> *"Conjuntos garantem automaticamente que não haja duplicatas e realizam verificações de pertinência (`in`) e operações matemáticas (como união e diferença) em tempo médio constante $O(1)$, enquanto em listas isso exigiria varredura linear $O(n)$."*

---

### Exercise 4: Inventory Master (`ex4/ft_inventory_system.py`)

* **Diretório:** `ex4/`
* **Arquivo:** `ft_inventory_system.py`
* **Conceito:** Dicionários (`dict`), pares chave-valor e agregação de dados.

#### Para que serve e Descrição
Processa um inventário de RPG a partir de parâmetros no formato `item:quantidade`. O programa descarta duplicatas e formatos inválidos, calcula o peso percentual de cada item no inventário total, identifica os itens mais e menos abundantes respeitando desempate pela ordem de aparição, e demonstra inserção de novos dados com `.update()`.

#### O que foi aprendido
* Estrutura de pares chave-valor em dicionários.
* Métodos embutidos de dicionário: `.keys()`, `.values()`, `.items()`, `.update()`.
* Preservação da ordem de inserção dos dicionários (desde o Python 3.7+).
* Resolução de empate (tie-breaker): utilizando operadores estritos (`>` e `<`), mantemos naturalmente o primeiro item encontrado na linha de comando.

#### Roteiro para Explicar na Defesa
> **"Como foi resolvido o critério de desempate para o item mais/menos abundante?"**  
> *"Dicionários no Python moderno preservam a ordem de inserção dos itens. Ao iterar sobre o dicionário usando comparação estrita `if quantity > most_qty`, se outro item tiver a mesma quantidade máxima, a condição não é satisfeita, mantendo a primeira ocorrência encontrada."*

---

### Exercise 5: Stream Wizard (`ex5/ft_data_stream.py`)

* **Diretório:** `ex5/`
* **Arquivo:** `ft_data_stream.py`
* **Conceito:** Geradores (`yield`), iteração sob demanda e consumo com `next()`.

#### Para que serve e Descrição
Simula uma engine de eventos de jogos em tempo real (ex: Fortnite processando milhões de cliques e movimentos). Em vez de carregar todos os dados na memória RAM de uma só vez, funções geradoras com a palavra-chave `yield` produzem eventos dinamicamente sob demanda. Em seguida, implementa-se um gerador consumidor que remove elementos aleatoriamente de uma lista até esvaziá-la.

#### O que foi aprendido
* A diferença fundamental entre `return` (finaliza a função e descarta o estado) e `yield` (pausa a execução, preserva o estado e retorna um valor intermediário).
* Protocolo iterador com a função `next()`.
* Criação de streams infinitos com uso de memória de ordem $O(1)$.
* Tipagem de geradores com `typing.Generator[YieldType, SendType, ReturnType]`.
* Consumo direto de um gerador dentro de um loop `for .. in ..`.

#### Roteiro para Explicar na Defesa
> **"Qual a grande vantagem de geradores na engenharia de dados?"**  
> *"A economia massiva de memória (Memory Footprint). Um gerador infinito que gera 1 bilhão de eventos consome a mesma quantidade de memória que um gerador de 1 evento, pois os dados são processados e liberados sob demanda (lazy evaluation)."*

---

### Exercise 6: Data Alchemist (`ex6/ft_data_alchemist.py`)

* **Diretório:** `ex6/`
* **Arquivo:** `ft_data_alchemist.py`
* **Conceito:** *List Comprehensions* e *Dict Comprehensions* em linha única.

#### Para que serve e Descrição
Demonstra a sintaxe idiomática e eficiente do Python para filtrar e transformar dados sem recorrer a loops `for` verbosos e acumuladores manuais:
1. Padronização de nomes (capitalização completa com `.capitalize()`).
2. Filtragem de dados preexistentes (`if name.istitle()`).
3. Geração de dicionários mapeando nomes a pontuações aleatórias.
4. Filtragem condicional de dicionários para extrair pontuações acima da média.

#### O que foi aprendido
* Sintaxe das List Comprehensions: `[expressao for item in iteravel if condicao]`.
* Sintaxe das Dict Comprehensions: `{chave: valor for item in iteravel if condicao]`.
* Escrita limpa e idiomática em uma única linha, mantendo conformidade com o PEP 8 (limite de 79 colunas).
* Ganho de performance em relação a loops manuais com `.append()`.

#### Roteiro para Explicar na Defesa
> **"Por que usar comprehension em vez de loop tradicional?"**  
> *"Além de deixar o código mais legível e conciso, as comprehensions são executadas diretamente em nível de bytecode otimizado em C dentro do interpretador CPython, sendo geralmente mais rápidas do que loops manuais com `.append()`."*

---

## 🛠️ Como Executar e Testar os Exercícios

### Teste do Exercise 0
```bash
python3 ex0/ft_command_quest.py
python3 ex0/ft_command_quest.py hello world 42
python3 ex0/ft_command_quest.py "Data Quest"
```

### Teste do Exercise 1
```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex1/ft_score_analytics.py
python3 ex1/ft_score_analytics.py ab ac
```

### Teste do Exercise 2
```bash
python3 ex2/ft_coordinate_system.py
# Insira: hello world
# Insira: 1.0 , 2.5, 3.0
# Insira: 4,abc,5
# Insira: 4,5,6
```

### Teste do Exercise 3
```bash
python3 ex3/ft_achievement_tracker.py
```

### Teste do Exercise 4
```bash
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
```

### Teste do Exercise 5
```bash
python3 ex5/ft_data_stream.py
```

### Teste do Exercise 6
```bash
python3 ex6/ft_data_alchemist.py
```

---

## 📋 Resumo das Coleções Python

| Coleção | Mutável? | Ordenada? | Permite Duplicatas? | Sintaxe | Uso Ideal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Lista (`list`)** | Sim | Sim | Sim | `[1, 2, 3]` | Sequências ordenadas e expansíveis. |
| **Tupla (`tuple`)** | Não | Sim | Sim | `(1, 2, 3)` | Registros estáticos, coordenadas e chaves seguras. |
| **Conjunto (`set`)** | Sim | Não | Não | `{1, 2, 3}` | Testes de pertinência ultra-rápidos e operações matemáticas. |
| **Dicionário (`dict`)** | Sim | Sim (3.7+) | Chaves não, valores sim | `{"k": "v"}` | Mapeamento chave-valor e buscas instantâneas por chave. |

