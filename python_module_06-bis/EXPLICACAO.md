# Guia de Estudo e Defesa — Python Module 06-bis ("Code Nexus")

Bem-vindo à nossa aula! Este documento foi escrito como se eu fosse seu professor sentando do seu lado para explicar **cada linha, cada palavra-chave e cada escolha** que fizemos no código. O objetivo aqui não é você decorar respostas, mas sim **entender de verdade** como o Python funciona por baixo dos panos para que, na hora da avaliação (e nos próximos projetos), você tenha total domínio e segurança.

---

## Parte 1: Dicionário de Conceitos e Instruções do Python

Antes de olhar cada exercício, vamos entender as ferramentas que usamos em quase todos os arquivos. Se o avaliador apontar para qualquer linha e perguntar *"O que é isso?"*, a resposta está aqui.

---

### 1. O que são `ABC` e `@abstractmethod`? (`from abc import ABC, abstractmethod`)

* **O problema que eles resolvem:** Imagine que você está criando um sistema onde vários tipos de processadores (`Numeric`, `Text`, `Log`) vão trabalhar juntos. Para que o sistema funcione, **todos eles** precisam ter obrigatoriamente um método `validate()` e um método `ingest()`. E se um programador criar um novo processador amanhã e esquecer de criar o método `validate()`? O programa só daria erro lá na frente, quando tentasse rodar esse método.
* **A solução (Classe Abstrata - ABC):** `ABC` significa *Abstract Base Class* (Classe Base Abstrata). Uma classe abstrata funciona como um **molde ou contrato**.
  * Ela **não pode ser instanciada diretamente** (você não pode fazer `p = DataProcessor("teste")`, o Python dá um `TypeError`). Ela só existe para que outras classes herdem dela.
  * Quando colocamos `@abstractmethod` em cima de um método na classe pai, estamos dizendo ao Python: *"Qualquer classe filha que herdar de mim é **obrigada** a escrever o seu próprio código para este método. Se ela não escrever, proíba a criação do objeto na mesma hora!"*
* **Por que escrevemos `pass` dentro do método abstrato?** Em Python, um bloco `def` não pode ficar vazio. A palavra `pass` significa literalmente "não faça nada / passe direto". Como a classe pai é só um contrato e quem vai escrever o código de verdade são as classes filhas, deixamos apenas `pass` na classe pai.

---

### 2. O que é um Decorador (`@`) e como funciona o `@property`?

Você viu coisas com `@` no código: `@abstractmethod`, `@property`, `@staticmethod`. Em Python, o símbolo `@` chama-se **decorador** (*decorator*). Ele é uma etiqueta que você cola em cima de uma função ou método para modificar a forma como o Python trata aquele método.

#### O `@property` (Propriedade Calculada)

Vamos olhar este trecho da classe `DataProcessor`:

```python
@property
def remaining(self) -> int:
    return len(self._data)
```

* **Como seria SEM `@property`:** Se fosse um método comum, para saber quantos itens restam você teria que chamar com parênteses, como uma ação: `proc.remaining()`.
* **O que o `@property` faz:** Ele "disfarça" um método para que ele se comporte como um **atributo comum** (uma variável do objeto), **sem parênteses**: você escreve `proc.remaining`, exatamente como escreve `proc.name` ou `proc.total`.
* **Por que não criamos simplesmente uma variável `self.remaining = 0` no `__init__`?**
  * Pense como um engenheiro: a quantidade de itens restantes na fila é sempre o tamanho da lista `self._data` (`len(self._data)`).
  * Se criássemos uma variável separada `self.remaining = 0`, toda vez que adicionássemos um item teríamos que lembrar de fazer `self.remaining += 1`, e toda vez que removêssemos um item no `output()`, teríamos que lembrar de fazer `self.remaining -= 1`. Se esquecêssemos em um único lugar, o número ficaria errado (dessincronizado com a lista real)!
  * Com `@property`, **nunca há erro**: toda vez que alguém lê `proc.remaining`, o Python calcula `len(self._data)` na hora e devolve o valor exato. Além disso, impede que alguém de fora faça `proc.remaining = 999` e estrague a contagem (pois propriedades sem um *setter* são somente-leitura!).

---

### 3. O que é `@staticmethod`?

No exercício 2 (`data_pipeline.py`), dentro de `CSVPlugin` e `JSONPlugin`, usamos:

```python
@staticmethod
def _escape(value: str) -> str:
    ...
```

* **Por que ele existe?** Repare que todos os métodos normais de uma classe começam recebendo `self` como primeiro parâmetro (`def process_output(self, data):`). O `self` é a referência para o próprio objeto, usada quando você precisa ler ou mudar variáveis daquele objeto (como `self.name` ou `self._data`).
* Mas a função `_escape` só recebe uma string `value` e devolve outra string com aspas tratadas. Ela **não usa nada do `self`**!
* Quando um método está dentro de uma classe só por organização (porque só aquela classe usa aquela função auxiliar), mas não precisa do `self`, colocamos `@staticmethod`. Assim o Python sabe que não precisa passar o `self` automaticamente quando chamamos `self._escape(value)`.

---

### 4. Por que alguns nomes começam com um sublinhado `_` (`_data`, `_store`, `_processors`)?

Em Python, não existem palavras como `private` ou `protected` (como em C++ ou Java). Em vez disso, os programadores Python usam uma **convenção oficial (PEP 8)**:

* **Sem sublinhado (`name`, `total`, `validate`, `output`):** É **público**. Qualquer código de fora pode usar à vontade.
* **Com 1 sublinhado na frente (`_data`, `_store`, `_processors`, `_invalid`):** É **interno / protegido**. É um aviso para outros programadores (e para o avaliador): *"Este atributo ou método é um detalhe interno de funcionamento da classe. Quem está fora da classe não deveria mexer diretamente em `proc._data`, deveria usar apenas os métodos públicos `ingest()` e `output()`."*
  * **Na defesa:** Se perguntarem por que `_data` tem `_`, diga: *"Para indicar encapsulamento: a fila interna não deve ser alterada diretamente por código externo, apenas pelos métodos `ingest` e `output`, protegendo os dados contra corrupção."*

---

### 5. O que são Type Hints (`: str`, `-> bool`, `Any`, `|`) e o `mypy`?

Python é uma linguagem de tipagem dinâmica (você não é obrigado a declarar tipos para o código rodar). Porém, em projetos profissionais (e nas regras da 42), usamos **Type Hints** (anotações de tipo) e a ferramenta **`mypy`** para checar o código antes mesmo de rodar.

* **`data: str`** → Diz que o parâmetro `data` espera receber uma string.
* **`-> bool`** → Diz que a função vai devolver (`return`) um booleano (`True` ou `False`).
* **`-> None`** → Diz que a função não devolve nada (como o `void` do C).
* **`int | float`** (disponível a partir do Python 3.10) → A barra vertical `|` significa **OU** (*Union type*). Então `int | float` significa *"aceita um inteiro OU um número decimal"*.
* **`list[int | float]`** → Uma lista onde os elementos dentro dela podem ser `int` ou `float` (inclusive misturados).
* **`tuple[int, str]`** → Uma tupla com exatamente dois elementos: o primeiro é um `int` (o rank) e o segundo é uma `str` (o valor).
* **`dict[str, str]`** → Um dicionário onde todas as chaves são `str` e todos os valores são `str`.
* **`Any` (`from typing import Any`)** → Significa *"Qualquer tipo"*. Usamos em `validate(self, data: Any) -> bool` porque a função de validação pode receber literalmente qualquer coisa do mundo exterior para testar se é válida ou não.

---

### 6. Como funcionam `isinstance()`, `all()`, `any()` e Comprehensions?

Essas funções built-in (nativas do Python) deixam o código super limpo e substituem vários `for` e `if` gigantes. Vamos destrinchar cada uma que usamos:

#### `isinstance(objeto, tipo)`
Pergunta ao Python: *"Este `objeto` é daquele `tipo` (ou de uma subclasse daquele tipo)?"*
* `isinstance(42, int)` → `True`
* `isinstance(3.14, (int, float))` → `True` (quando passamos uma tupla de tipos, ele testa se é de **algum** daqueles tipos).

#### A pegadinha do `bool` em Python (`is_number`):
Olhe esta linha do nosso código:
```python
def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)
```
* **Por que temos `and not isinstance(value, bool)`?**
  Por uma razão histórica do Python, a classe `bool` (`True` e `False`) **herda da classe `int`**! Em Python, `True` vale `1` e `False` vale `0`. Se você rodar `isinstance(True, int)`, o Python responde **`True`**!
  Se não colocássemos `and not isinstance(value, bool)`, o `NumericProcessor` aceitaria `True` e `False` como se fossem números! Essa é uma pergunta clássica de avaliador — mostrar que você sabe disso ganha muitos pontos.

#### `all(...)` e `any(...)`
* **`all(condição for item in lista)`**: Devolve `True` somente se **TODOS** os itens da lista cumprirem a condição. Se um único falhar, ele para na hora e devolve `False`.
  * No `NumericProcessor.validate`:
    ```python
    if isinstance(data, list):
        return all(is_number(item) for item in data)
    ```
    Tradução para português: *"Se `data` for uma lista, verifique se **todos** os itens dentro de `data` são números."*
  * No `is_log`:
    ```python
    all(isinstance(k, str) and isinstance(v, str) for k, v in value.items())
    ```
    Tradução: *"Percorra todas as chaves (`k`) e valores (`v`) do dicionário (`value.items()`) e verifique se **todas** as chaves são strings e **todos** os valores são strings."*
* **`any(condição for item in sequencia)`**: Devolve `True` se **PELO MENOS UM** item cumprir a condição.
  * No `CSVPlugin._escape`:
    ```python
    if any(char in value for char in ',"\n'):
    ```
    Tradução: *"Se **qualquer** um dos caracteres `,`, `"` ou quebra de linha `\n` estiver dentro do texto `value`..."*

---

### 7. O que é `super().__init__(...)`?

Quando `NumericProcessor` herda de `DataProcessor`, a classe pai (`DataProcessor`) tem um método `__init__` que cria os atributos `self.name`, `self.total = 0` e `self._data = []`.
Quando escrevemos na classe filha:

```python
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")
```

`super()` significa *"acesse a superclasse (a classe pai)"*. Então `super().__init__("Numeric Processor")` chama o construtor da classe pai passando o nome `"Numeric Processor"`, para que a classe pai configure `self.name`, `self.total` e `self._data` para nós, sem termos que repetir esse código nas 3 classes filhas!

---

## Parte 2: Explicação Passo a Passo de Cada Exercício

---

### Exercício 0 — `data_processor.py` (Classes Abstratas e Sobrescrita)

#### Como a fila FIFO e o Rank funcionam:
1. Cada processador começa com `self.total = 0` e `self._data = []` (uma lista vazia que guarda tuplas `(rank, texto)`).
2. Toda vez que um item individual é guardado pelo método auxiliar `self._store(value)`:
   ```python
   def _store(self, value: str) -> None:
       self._data.append((self.total, value))
       self.total += 1
   ```
   * O primeiro item entra com `(0, valor)` e `self.total` sobe para `1`.
   * O segundo item entra com `(1, valor)` e `self.total` sobe para `2`, e assim por diante.
3. Quando alguém chama `output()`:
   ```python
   def output(self) -> tuple[int, str]:
       if not self._data:
           raise IndexError(f"No data left on {self.name}")
       return self._data.pop(0)
   ```
   * `self._data.pop(0)` remove e devolve o elemento na **posição 0** da lista — ou seja, o **primeiro que entrou (o mais antigo)**! Isso se chama fila **FIFO** (*First-In, First-Out*: o primeiro a entrar é o primeiro a sair).
   * Como o rank já foi salvo dentro da tupla `(rank, valor)` na hora em que o dado entrou, mesmo que itens sejam removidos da lista, os próximos itens que entrarem continuam usando `self.total` (que nunca diminui: 0, 1, 2, 3, 4...).

#### Como o `ingest` protege contra corrupção de dados:
Olhe as 4 linhas do `ingest` em todas as subclasses:
```python
def ingest(self, data: int | float | list[int | float]) -> None:
    if not self.validate(data):
        raise ValueError("Improper numeric data")
    items = data if isinstance(data, list) else [data]
    for item in items:
        self._store(str(item))
```
1. **Validação antes de tudo:** Se o usuário passar uma lista `[1, 2, "erro", 4]` direto para o `ingest` sem chamar `validate` antes, o `if not self.validate(data)` testa a lista **inteira** antes de guardar qualquer número. Como `"erro"` falha, ele levanta `ValueError` imediatamente, e os números `1` e `2` **não** entram na fila. Ou entra tudo válido, ou não entra nada (operação atômica).
2. **Normalização para lista (`items = data if isinstance(data, list) else [data]`):** Esse operador ternário evita ter que escrever um `if/else` duplicado. Se `data` já for uma lista (ex: `[1, 2, 3]`), `items` é `[1, 2, 3]`. Se `data` for um número solto (ex: `42`), ele coloca dentro de uma lista de 1 elemento: `[42]`. Assim, logo abaixo, um único `for item in items:` funciona para os dois casos!

#### Por que a linha `numbers: list[int | float] = [1, 2, 3, 4, 5]` no `main` tem anotação de tipo?
Se você escrever apenas `numbers = [1, 2, 3, 4, 5]`, o `mypy` deduz que `numbers` é do tipo `list[int]`. Para o `mypy`, uma `list[int]` não é igual a uma `list[int | float]` (porque em Python listas são mutáveis/invariantes). Ao declarar explicitamente `numbers: list[int | float]`, dizemos ao `mypy` que aquela lista aceita `int` e `float`, casando perfeitamente com a assinatura do `ingest`.

---

### Exercício 1 — `data_stream.py` (Polimorfismo e `for ... else`)

Neste exercício entra a classe **`DataStream`**, que recebe uma lista com dados de vários tipos misturados e precisa entregar cada dado para o processador certo.

#### O segredo do `process_stream`:
```python
def process_stream(self, stream: list[Any]) -> None:
    for element in stream:
        for proc in self._processors:
            if proc.validate(element):
                try:
                    proc.ingest(element)
                except ValueError as error:
                    print(f"DataStream error - {error}")
                break
        else:
            print("DataStream error - "
                  f"Can't process element in stream: {element}")
```

Vamos entender duas coisas fundamentais aqui:

1. **Onde está o Polimorfismo?**
   * *Polimorfismo* vem do grego "muitas formas".
   * Repare que dentro do `DataStream`, nós **nunca** perguntamos qual é o tipo do dado nem qual é a classe do processador (não existe `if isinstance(element, int): usa NumericProcessor`).
   * Para o `DataStream`, todos os itens de `self._processors` são apenas `DataProcessor`. Ele simplesmente faz a mesma pergunta para cada um: `if proc.validate(element):` e depois `proc.ingest(element)`.
   * Como `NumericProcessor`, `TextProcessor` e `LogProcessor` têm a mesma interface (herdada de `DataProcessor`), o Python chama automaticamente o método da classe certa em tempo de execução.

2. **Como funciona o `for ... else` em Python?**
   * Muita gente que vem do C estranha ver um `else` alinhado com o `for` (e não com o `if`!).
   * Em Python, todo laço `for` pode ter um bloco `else`. A regra é super simples: **o bloco `else` do `for` só executa se o laço `for` terminou até o fim SEM encontrar nenhum `break`**.
   * Veja como fica elegante:
     * Para cada processador registrado, testamos `if proc.validate(element):`.
     * Se algum processador aceitar o elemento, ele ingere o elemento e dá um **`break`** (sai do laço de processadores e pula o `else`).
     * Se o laço testar todos os processadores registrados (ou se a lista de processadores estiver vazia) e **nenhum** aceitar (ou seja, nenhum der `break`), o Python entra no `else:` e imprime `DataStream error - Can't process element in stream: ...`!

---

### Exercício 2 — `data_pipeline.py` (`Protocol` e Duck Typing)

Aqui aprendemos a diferença entre herança tradicional (**ABC**) e tipagem estrutural (**Protocol / Duck Typing**).

#### O que é Duck Typing e `Protocol` (`from typing import Protocol`)?
Existe um ditado famoso na programação: *"Se anda como um pato e faz quack como um pato, então é um pato."* (*Duck Typing*).

Olhe como definimos o `ExportPlugin`:
```python
class ExportPlugin(Protocol):
    """Any object with this method is an export plugin (duck typing)."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...
```
*(Nota: os três pontinhos `...` em Python chamam-se `Ellipsis`. Dentro de um `Protocol`, funcionam exatamente como o `pass`: indicam que o método é só uma assinatura, sem corpo).*

Agora olhe como definimos os plugins `CSVPlugin` e `JSONPlugin`:
```python
class CSVPlugin:
    ...
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...
```
* **Reparou no detalhe mais importante?** `class CSVPlugin:` **NÃO herda de `ExportPlugin`**! Não está escrito `class CSVPlugin(ExportPlugin):`.
* Mesmo sem herdar, quando fazemos `stream.output_pipeline(3, CSVPlugin())`, tanto o Python quanto o `mypy` aceitam sem reclamar!
* **Por quê?** Porque `ExportPlugin` herda de `Protocol`. Um `Protocol` diz ao `mypy`: *"Não exija que a classe seja filha de `ExportPlugin`. Apenas olhe a **estrutura** dela: ela tem um método chamado `process_output` que recebe `list[tuple[int, str]]` e retorna `None`? Se tiver, aceite!"*

#### Como funciona o `output_pipeline`:
```python
def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    for proc in self._processors:
        data: list[tuple[int, str]] = []
        while len(data) < nb and proc.remaining > 0:
            data.append(proc.output())
        if data:
            plugin.process_output(data)
```
* Para cada processador registrado (`Numeric`, depois `Text`, depois `Log`), criamos uma lista temporária `data = []`.
* Enquanto ainda não pegamos `nb` itens (`len(data) < nb`) **E** o processador ainda tiver itens sobrando na fila (`proc.remaining > 0`), tiramos o item mais antigo com `proc.output()` e colocamos em `data`.
  * Por que checamos `proc.remaining > 0`? Porque no exemplo do PDF, o `LogProcessor` só tem **2** itens na fila, mas o `main` pede para exportar **3** (`output_pipeline(3, ...)`). Se tentássemos chamar `output()` 3 vezes sem checar `proc.remaining > 0`, na terceira vez a fila estaria vazia e daria erro! Com `proc.remaining > 0`, ele pega os 2 itens que existem e para com segurança.
* Por fim, `if data:` garante que só chamamos o plugin se pelo menos 1 item foi extraído.

#### Como o CSV e o JSON são montados:
* **No `CSVPlugin`:**
  ```python
  print(",".join(self._escape(value) for _, value in data))
  ```
  * Cada elemento de `data` é uma tupla `(rank, value)`.
  * No `for _, value in data`, usamos `_` como nome da primeira variável porque o CSV não usa o `rank`, só o `value` (em Python, usar `_` para uma variável significa *"estou ignorando este valor de propósito"*).
  * `",".join(...)` pega todos os valores e junta tudo numa única string separada por vírgula: `"3.14,-1,2.71"`.
* **No `JSONPlugin`:**
  ```python
  items = [f'"item_{rank}": "{self._escape(value)}"'
           for rank, value in data]
  print("{" + ", ".join(items) + "}")
  ```
  * Aqui usamos tanto o `rank` quanto o `value` para criar strings no formato `"item_3": "42"`, depois juntamos todas com `", "` e colocamos chaves `{` e `}` em volta.

---

### Exercício 3 — Pacote `ex3/`, `battle.py` e `capacitor.py` (Abstract Factory, Capability e Pacotes)

Aqui o projeto deixa de ser um arquivo único e passa a usar um **pacote Python (`ex3/`)**.

#### 1. Como funciona um Pacote Python e o `__init__.py`?
* Qualquer pasta que tenha um arquivo chamado `__init__.py` dentro dela vira um **pacote** que pode ser importado com `import ex3` ou `from ex3 import ...`.
* **Imports relativos (com ponto `.`):** Dentro dos arquivos da pasta `ex3/` (como `factories.py`), você vê:
  ```python
  from .creature import Creature
  from .creatures import Flameling, Morphagon, Pyrodon, Shiftling
  ```
  O ponto `.` antes do nome significa **"procure dentro desta mesma pasta (`ex3/`)"**.
* **O papel do `ex3/__init__.py` e da lista `__all__`:**
  O subject exige: *"Your ex3 package must only expose the factories, never the concrete entities."*
  Por isso, o nosso `ex3/__init__.py` tem apenas:
  ```python
  from .factories import CreatureFactory, FlameFactory, TransformCreatureFactory

  __all__ = ["CreatureFactory", "FlameFactory", "TransformCreatureFactory"]
  ```
  * O que isso faz? Quando o `battle.py` (que está fora da pasta `ex3`) faz `from ex3 import FlameFactory`, o Python olha o `ex3/__init__.py`.
  * A variável especial `__all__` define a lista oficial do que é público naquele pacote. As classes concretas (`Flameling`, `Pyrodon`, `Shiftling`, `Morphagon`) **não** estão no `__init__.py`. Assim, quem usa o pacote `ex3` é forçado a usar as **Fábricas** para criar criaturas, em vez de instanciar `Flameling()` diretamente!

#### 2. O Padrão Abstract Factory (`CreatureFactory`)
* **O que é:** Uma fábrica (`FlameFactory` ou `TransformCreatureFactory`) é um objeto cuja única responsabilidade é criar outros objetos de uma mesma família (`create_base()` cria a criatura inicial e `create_evolved()` cria a evoluída), devolvendo sempre o tipo abstrato `Creature`.
* **Por que usar isso?** Olhe a função `test_factory(factory: CreatureFactory)` no `battle.py`:
  ```python
  def test_factory(factory: CreatureFactory) -> None:
      print("Testing factory")
      for creature in (factory.create_base(), factory.create_evolved()):
          print(creature.describe())
          print(creature.attack())
  ```
  Essa única função consegue testar **qualquer família de criaturas** (fogo, transformação, ou uma família aquática que você crie na hora da avaliação) sem precisar saber o nome das classes concretas!

#### 3. O Padrão Capability e a Herança Múltipla (`Shiftling` e `Morphagon`)
* Algumas criaturas (`Shiftling` e `Morphagon`) têm uma habilidade extra: elas podem se transformar (`transform()`) e voltar ao normal (`revert()`). Já `Flameling` e `Pyrodon` **não** têm essa habilidade.
* Para resolver isso sem estragar a classe `Creature`, criamos uma classe abstrata separada chamada `TransformCapability(ABC)`, que **não herda de `Creature`**. Ela guarda apenas o atributo `self.transformed: bool = False` e exige os métodos `transform()` e `revert()`.
* Então, `Shiftling` e `Morphagon` usam **Herança Múltipla** (herdam das duas classes ao mesmo tempo):
  ```python
  class Shiftling(Creature, TransformCapability):
      def __init__(self) -> None:
          Creature.__init__(self, "Shiftling", "Normal")
          TransformCapability.__init__(self)
  ```
  * **Por que chamamos `Creature.__init__(self, ...)` e `TransformCapability.__init__(self)` pelo nome em vez de `super().__init__()`?**
    Porque `Shiftling` tem **dois pais** diferentes! O primeiro pai (`Creature`) precisa inicializar `self.name` e `self.creature_type`, enquanto o segundo pai (`TransformCapability`) precisa inicializar `self.transformed = False`. Chamar o `__init__` de cada pai explicitamente pelo nome deixa 100% claro o que cada classe pai está inicializando.

---

### Exercício 4 — Pacote `ex4/` e `tournament.py` (Abstract Strategy, Exceção Dedicada e Torneio)

#### 1. O Padrão Strategy (`BattleStrategy`)
No exercício 3 vimos que criaturas comuns só atacam (`attack()`), enquanto criaturas com `TransformCapability` podem fazer um combo (`transform()` → `attack()` → `revert()`).
Como fazer um torneio onde qualquer criatura possa lutar sem que o código do torneio tenha um monte de `if/else`?
* Criamos o padrão **Strategy** (Estratégia): encapsulamos "a forma de lutar" dentro de objetos de estratégia (`NormalStrategy` e `AggressiveStrategy`).
* O torneio não precisa saber se a estratégia é normal ou agressiva; ele só chama `strategy.act(creature)`.
* Dentro da `AggressiveStrategy`, como ela sabe se a criatura pode usar essa estratégia?
  ```python
  def is_valid(self, creature: Creature) -> bool:
      return isinstance(creature, TransformCapability)
  ```
  Ela testa se a criatura tem a **capacidade** (`TransformCapability`) usando `isinstance`, e **nunca** testa se a criatura é da família `Shiftling` ou `Morphagon`. Assim, se amanhã você criar outra família completamente diferente que também herde de `TransformCapability`, a `AggressiveStrategy` já vai funcionar com ela automaticamente!

#### 2. A Exceção Dedicada (`InvalidStrategyError`)
```python
class InvalidStrategyError(Exception):
    """Raised when a strategy is used with a creature it does not fit."""
```
* Em Python, para criar o seu próprio tipo de erro (exceção), basta criar uma classe que herde de `Exception`. Não precisa escrever nada dentro dela (a classe `Exception` do Python já sabe guardar a mensagem de texto que passamos quando fazemos `raise InvalidStrategyError("mensagem")`).
* **Por que criar uma exceção própria em vez de usar `ValueError`?** Porque no `tournament.py`, quando fazemos `except InvalidStrategyError as error:`, temos certeza absoluta de que estamos capturando **apenas** o erro de estratégia incompatível com a criatura, sem esconder por acidente outros erros do Python.

#### 3. A lógica dos dois laços `for` no `tournament.py` (Todos contra Todos, sem repetição)
Olhe como o `battle()` em `tournament.py` faz as lutas:
```python
for i in range(len(fighters)):
    for j in range(i + 1, len(fighters)):
        first, first_strategy = fighters[i]
        second, second_strategy = fighters[j]
```
* **Por que o segundo `for` começa em `i + 1` (`range(i + 1, len(fighters))`)?**
  Imagine que temos 3 lutadores na lista: índice `0` (A), índice `1` (B) e índice `2` (C).
  * Quando `i = 0` (A): `j` começa em `0 + 1 = 1` e vai até `2`.
    * Luta `0 vs 1` (**A vs B**)
    * Luta `0 vs 2` (**A vs C**)
  * Quando `i = 1` (B): `j` começa em `1 + 1 = 2` e vai até `2`.
    * Luta `1 vs 2` (**B vs C**)
  * Quando `i = 2` (C): `j` começa em `2 + 1 = 3` (não roda, pois a lista acaba no 2).
* Veja que mágica: começando `j` em `i + 1`, **ninguém nunca luta contra si mesmo** (`i` nunca é igual a `j`) e **nenhuma luta se repete invertida** (depois de A vs B, nunca acontece B vs A). Essa é uma exigência explícita da régua de avaliação!

---

## Parte 3: Roteiro de Respostas para as Perguntas da Avaliação

Na folha de avaliação que o seu colega vai seguir, existem perguntas obrigatórias. Abaixo está como você pode responder cada uma com suas próprias palavras de forma clara e direta:

1. **Ex0 — "Por que classes base abstratas (ABC) são úteis?"**
   * **Resposta:** *"Elas servem para criar um contrato obrigatório para uma família de classes e reaproveitar código comum. Ao herdar de `ABC` e usar `@abstractmethod` em `validate` e `ingest`, o Python impede que alguém crie uma subclasse esquecendo de implementar esses métodos (dá erro na hora de instanciar). Além disso, colocamos o método concreto `output()` na classe base uma única vez e todas as subclasses já herdam esse funcionamento pronto."*

2. **Ex1 — "Como o polimorfismo permite tratar diferentes tipos de dados no stream sem conhecer as implementações?"**
   * **Resposta:** *"O `DataStream` não sabe que existem `NumericProcessor`, `TextProcessor` ou `LogProcessor`; ele só enxerga a classe base `DataProcessor`. Como todas as subclasses têm os mesmos métodos `validate()` e `ingest()`, o `DataStream` apenas percorre a lista chamando `proc.validate(element)` e `proc.ingest(element)`, e o Python executa o método específico de cada objeto. Se eu quiser adicionar um novo tipo de dado amanhã, só crio uma nova subclasse e registro no stream, sem alterar uma única linha da classe `DataStream`."*

3. **Ex2 — "Qual a diferença entre `ABC` e `Protocol` (duck typing), e por que um sistema de plugins prefere `Protocol`?"**
   * **Resposta:** *"Com `ABC` (tipagem nominal), uma classe é obrigada a herdar explicitamente da classe base para ser aceita. Já com `Protocol` (tipagem estrutural / duck typing), não precisa de herança: qualquer classe que tenha o método `process_output` com os parâmetros certos já é aceita como um `ExportPlugin`. Para plugins isso é ótimo porque desacopla o sistema: quem cria um plugin novo (como `CSVPlugin` ou `JSONPlugin`, ou até uma biblioteca externa) não precisa herdar nem importar a nossa classe `ExportPlugin`."*

4. **Ex3 — "O que quebraria, ou ficaria impossível, se `transform()` e `revert()` tivessem sido colocados dentro da classe base `Creature`?"**
   * **Resposta:** *"Três coisas ruins aconteceriam: primeiro, toda criatura do jogo (inclusive `Flameling` e `Pyrodon`, que não se transformam) seria obrigada a implementar métodos `transform` e `revert` inúteis ou que dão erro. Segundo, perderíamos a capacidade de descobrir quem realmente se transforma usando `isinstance(creature, TransformCapability)`, porque toda criatura seria uma `Creature`. E terceiro, se quiséssemos criar outras habilidades no futuro (como voar ou nadar), a classe `Creature` ficaria gigante. Separando em uma `Capability`, só herda quem realmente tem a habilidade."*

5. **Ex4 — "O código do torneio nunca verifica a qual família uma entidade pertence, mas cada uma luta diferente. Para onde foi essa decisão e o que você ganha quando uma nova capability é adicionada?"**
   * **Resposta:** *"A decisão foi movida para dentro das classes de estratégia (`BattleStrategy`). O torneio apenas chama `strategy.act(creature)`. É a estratégia que executa os movimentos certos e usa `isinstance(creature, TransformCapability)` para checar se a criatura tem a habilidade necessária. O grande ganho é que, se adicionarmos uma nova habilidade e uma nova estratégia amanhã, o código do torneio (`tournament.py`) continua funcionando sem precisar mudar nenhuma linha."*
