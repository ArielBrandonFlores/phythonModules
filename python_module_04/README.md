# Python Module 04: Data Archivist - Digital Preservation in the Cyber Archives

Guia completo e documentação explicativa dos exercícios do módulo 04 da 42. Este material foi estruturado para servir de estudo detalhado, explicando cada linha de raciocínio, decisões de implementação e preparando você para responder com segurança a qualquer pergunta durante a avaliação (*peer review*).

---

## 📌 Sumário
1. [Visão Geral e Objetivos do Módulo](#1-visão-geral-e-objetivos-do-módulo)
2. [Estrutura do Repositório](#2-estrutura-do-repositório)
3. [Regras Críticas e Restrições](#3-regras-críticas-e-restrições)
4. [Explicação Detalhada do Código](#4-explicação-detalhada-do-código)
   - [Exercício 0: Ancient Text Recovery (`ex0/ft_ancient_text.py`)](#exercício-0-ancient-text-recovery)
   - [Exercício 1: Archive Creation (`ex1/ft_archive_creation.py`)](#exercício-1-archive-creation)
   - [Exercício 2: Stream Management (`ex2/ft_stream_management.py`)](#exercício-2-stream-management)
   - [Exercício 3: Vault Security (`ex3/ft_vault_security.py`)](#exercício-3-vault-security)
5. [Guia de Defesa e Perguntas Frequentes (Peer Review)](#5-guia-de-defesa-e-perguntas-frequentes-peer-review)
6. [Instruções de Execução e Testes](#6-instruções-de-execução-e-testes)

---

## 1. Visão Geral e Objetivos do Módulo

O objetivo central deste módulo é dominar as operações fundamentais de entrada e saída (I/O) em Python, progredindo do gerenciamento manual de recursos para a abstração moderna via *Context Managers*:

1. **Manipulação Básica de Arquivos**: Abertura, leitura, escrita e fechamento explícito com `open()`, `.read()`, `.write()` e `.close()`.
2. **Gerenciamento Manual de Recursos e Exceções**: Uso correto de blocos `try ... except ... finally` para garantir que arquivos abertos sejam sempre fechados, evitando vazamento de descritores de arquivo (*file descriptor leaks*).
3. **Fluxos Padrão do Sistema (Streams)**: Diferenciação e controle de `sys.stdin` (entrada padrão), `sys.stdout` (saída padrão) e `sys.stderr` (saída de erros com prefixo `[STDERR]`).
4. **Context Managers (`with`)**: Compreensão de como o protocolo de contexto (`__enter__` e `__exit__`) simplifica o gerenciamento de recursos e garante liberação automática de memória e descritores.

---

## 2. Estrutura do Repositório

```text
python_module_04/
├── .gitignore                  # Impede o envio de arquivos não solicitados ao Git
├── RULES.md                    # Regras e especificações do subject
├── README.md                   # Este guia de estudo completo
├── ex0/
│   └── ft_ancient_text.py      # Exercício 0: Leitura manual estilo 'cat'
├── ex1/
│   └── ft_archive_creation.py  # Exercício 1: Transformação e gravação
├── ex2/
│   └── ft_stream_management.py # Exercício 2: Uso direto de fluxos (stdin, stdout, stderr)
└── ex3/
    └── ft_vault_security.py    # Exercício 3: Função segura usando 'with'
```

---

## 3. Regras Críticas e Restrições

- **Python 3.10+**: Uso de recursos modernos de tipagem (ex.: `str | None`, `tuple[bool, str]`).
- **flake8**: Conformidade rigorosa com PEP 8 (linhas de no máximo 79 caracteres, espaçamentos adequados, sem variáveis/imports não utilizados).
- **mypy**: Todas as funções possuem type hints explícitos para parâmetros e retornos.
- **A Regra de Ouro do `with`**:
  - Nos exercícios **0, 1 e 2**, o uso da instrução `with` é **estritamente PROIBIDO**. Os arquivos devem ser manipulados manualmente com `open()` e `.close()` dentro de blocos `try ... except ... finally`.
  - No exercício **3**, o uso do `with` é **OBRIGATÓRIO**.
- **A Regra do `input()` no Ex2**: No exercício 2, a função built-in `input()` é **PROIBIDA**. A leitura do teclado deve ser feita diretamente via `sys.stdin.readline()`.

---

## 4. Explicação Detalhada do Código

---

### Exercício 0: Ancient Text Recovery
**Arquivo**: `ex0/ft_ancient_text.py`

#### Objetivo:
Simular o comportamento do utilitário `cat` do Unix, lendo um arquivo passado via linha de comando (`sys.argv[1]`) e tratando possíveis falhas (arquivo inexistente ou sem permissão de leitura) sem deixar o programa quebrar (*crash*).

#### Código e Lógica:

```python
import sys
import typing


def recover_ancient_text(filename: str) -> None:
    """Read and display the contents of an archive file safely without with."""
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content: str = file_obj.read()
        print("---")
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)
        print("---")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")
```

#### Explicação Passo a Passo:
1. **`file_obj: typing.IO[str] | None = None`**:
   - Inicializamos a variável antes do bloco `try`. Se `open()` falhar (ex.: `FileNotFoundError`), `file_obj` continuará `None`.
2. **`try`**:
   - `file_obj = open(filename, "r")`: Abre o arquivo em modo leitura textual.
   - `content = file_obj.read()`: Carrega todo o conteúdo do arquivo como `str`.
   - `print(content, end="" if content.endswith("\n") else "\n")`: Garante que, se o arquivo já terminar com `\n`, o `print()` não adicione uma linha em branco desnecessária antes do delimitador `---`.
3. **`except OSError as error`**:
   - `OSError` é a classe base para erros do sistema de arquivos (`FileNotFoundError`, `PermissionError`, etc.).
   - Capturamos o erro e exibimos no formato exigido pelo subject: `Error opening file '<file>': <detalhes>`.
4. **`finally`**:
   - Este bloco é **garantido para rodar sempre**, quer tenha ocorrido erro ou não.
   - Verificamos `if file_obj is not None:`: só fechamos o arquivo se ele tiver sido de fato aberto. Em caso de sucesso, chama `file_obj.close()` e exibe `File '<filename>' closed.`.
5. **`main() -> None`**:
   - Verifica `if len(sys.argv) != 2:`. Se o usuário não passar exatamente 1 arquivo, exibe a mensagem de ajuda: `Usage: ft_ancient_text.py <file>`.

---

### Exercício 1: Archive Creation
**Arquivo**: `ex1/ft_archive_creation.py`

#### Objetivo:
Evolução do Exercício 0. Lê o arquivo, adiciona o caractere de preservação `#` ao fim de cada linha, exibe os dados transformados e pergunta ao usuário via `input()` se ele deseja salvar em um novo arquivo.

#### Funções e Lógica:

1. **`transform_data(content: str) -> str`**:
   ```python
   def transform_data(content: str) -> str:
       """Append the '#' character to the end of each line."""
       lines: list[str] = content.splitlines()
       if not lines:
           return ""
       transformed_lines: list[str] = [f"{line}#" for line in lines]
       return "\n".join(transformed_lines) + "\n"
   ```
   - `content.splitlines()`: Divide a string em uma lista de linhas, removendo as quebras de linha (`\n`).
   - `[f"{line}#" for line in lines]`: Uma *list comprehension* simples e idiomática que anexa `#` ao término de cada linha.
   - `"\n".join(...) + "\n"`: Junta as linhas modificadas e assegura a quebra de linha final compatível com arquivos POSIX.

2. **`save_archive_data(filename: str, content: str) -> None`**:
   - Abre o arquivo em modo escrita (`"w"`).
   - Se o arquivo já existir, o modo `"w"` sobrescreve (*truncate*); se não existir, cria um novo (conforme o requisito: *"Create the file or replace it if it already exists"*).
   - Grava com `.write(content)` e fecha no `finally`.

3. **`recover_and_preserve(filename: str) -> None`**:
   - Reutiliza a leitura do Ex0 com o cabeçalho `=== Cyber Archives Recovery & Preservation ===`.
   - Exibe a seção de dados transformados com `Transform data:`.
   - Pede o nome do arquivo com `new_filename = input("Enter new file name (or empty): ")`.
   - Se o usuário der apenas Enter (`not new_filename`), exibe `Not saving data.`.
   - Caso contrário, chama `save_archive_data`.

---

### Exercício 2: Stream Management
**Arquivo**: `ex2/ft_stream_management.py`

#### Objetivo:
Gerenciar diretamente os descritores de fluxo padrão do sistema operacional:
- `sys.stdin`: Canal de entrada.
- `sys.stdout`: Canal de saída padrão.
- `sys.stderr`: Canal de saída de erros.

#### Restrições Críticas:
- **Proibido usar `input()`**.
- Mensagens de erro de exceção devem ir para o canal de erro padrão com prefixo `[STDERR]`.
- **Proibido usar `with`**.

#### Funções e Lógica:

1. **`read_user_input(prompt: str) -> str`**:
   ```python
   def read_user_input(prompt: str) -> str:
       """Prompt user and read one line from sys.stdin without using input()."""
       sys.stdout.write(prompt)
       sys.stdout.flush()
       line: str = sys.stdin.readline()
       if line.endswith("\r\n"):
           return line[:-2]
       if line.endswith("\n"):
           return line[:-1]
       return line
   ```
   - **Por que `flush()`?** Diferente do `print()`, o `sys.stdout.write()` utiliza buffer e pode não exibir o texto na tela imediatamente se não houver um `\n`. O `sys.stdout.flush()` força a descarga imediata do buffer para o terminal.
   - **`sys.stdin.readline()`**: Lê uma linha digitada até que o usuário pressione Enter.
   - Como `readline()` inclui a quebra de linha digitada (`\n`), usamos fatiamento (`[:-1]`) para removê-la, reproduzindo com fidelidade o comportamento do `input()`.

2. **Envio de Erros para `sys.stderr`**:
   ```python
   except OSError as error:
       print(
           f"[STDERR] Error opening file '{filename}': {error}",
           file=sys.stderr,
       )
   ```
   - O argumento `file=sys.stderr` garante que o erro vá para o canal de erros. Se alguém rodar o programa redirecionando a saída padrão para um arquivo (`python3 ft_stream_management.py foo > out.txt`), a mensagem de erro continuará aparecendo na tela do terminal porque ela sai no `stderr`, não no `stdout`.

3. **Fluxo de Falha ao Salvar**:
   - Se tentar salvar em um arquivo protegido (ex.: `/etc/passwd`), a exceção é capturada:
     - Imprime o erro no `sys.stderr` com prefixo `[STDERR]`.
     - Imprime `Data not saved.` no `sys.stdout`.

---

### Exercício 3: Vault Security
**Arquivo**: `ex3/ft_vault_security.py`

#### Objetivo:
Implementar uma função segura de manipulação de arquivos utilizando o statement `with` (*Context Manager*).

#### Especificação da Função:
- **Nome**: `secure_archive`
- **Parâmetros**:
  - `filename: str` (obrigatório): Caminho do arquivo.
  - `action: str | int = "read"` (opcional): Ação a ser executada (`"read"` / `0` ou `"write"` / `1`). Padrão: `"read"`.
  - `content: str | None = None` (opcional): Conteúdo a ser gravado em caso de escrita.
- **Retorno**: `tuple[bool, str]`
  - Sucesso na leitura: `(True, <conteúdo do arquivo>)`
  - Sucesso na escrita: `(True, 'Content successfully written to file')`
  - Falha: `(False, '<mensagem de erro>')`

#### Código da Função:

```python
def secure_archive(
    filename: str,
    action: str | int = "read",
    content: str | None = None,
) -> tuple[bool, str]:
    """Provide safe access to a file using context manager (with)."""
    try:
        if action in ("read", 0):
            with open(filename, "r") as archive_file:
                return (True, archive_file.read())
        elif action in ("write", 1):
            with open(filename, "w") as archive_file:
                if content is not None:
                    archive_file.write(content)
                return (True, "Content successfully written to file")
        return (False, f"Invalid action: {action}")
    except OSError as error:
        return (False, str(error))
```

#### Por que usar o `with` (Context Manager)?
- Sem `with`: precisamos de `try`, `except` e `finally` manuais com checagem se o arquivo não é `None` para chamar `.close()`.
- Com `with`: o Python automaticamente invoca o método especial `__enter__()` ao iniciar o bloco e o método `__exit__()` ao sair dele. **Mesmo que ocorra uma exceção grave no meio do bloco, o método `__exit__()` do arquivo é chamado garantidamente, fechando o arquivo sem risco de vazamento de descritores.**

#### Testes de Demonstração no `main()`:
O bloco `main()` executa e imprime as 4 situações demonstradas no subject:
1. Leitura de arquivo inexistente: `(False, "[Errno 2] No such file or directory: ...")`
2. Leitura de arquivo inacessível (sem permissão): `(False, "[Errno 13] Permission denied: ...")`
3. Leitura de arquivo regular: `(True, '<conteúdo fragmentado>')`
4. Escrita em novo arquivo: `(True, 'Content successfully written to file')`

---

## 5. Guia de Defesa e Perguntas Frequentes (Peer Review)

Durante a sua avaliação, prepare-se para responder às seguintes perguntas:

### P1: Qual é o tipo de retorno da função built-in `open()`?
> **Resposta**: Em modo texto padrão (`"r"` ou `"w"`), `open()` retorna uma instância de `_io.TextIOWrapper`. Se for aberto em modo binário (`"rb"` ou `"wb"`), retorna um `_io.BufferedReader` ou `_io.BufferedWriter`. Todos eles herdam da classe abstrata `io.IOBase` (representada genericamente pelo tipo `typing.IO[str]` em type hints).

### P2: Por que você não usou `with` nos três primeiros exercícios?
> **Resposta**: Porque o subject proíbe expressamente o uso de `with` antes do Exercício 3 (*"the use of the with statement will be introduced in exercise 3. You must not use it before then"*). O propósito didático é fazer o aluno compreender como funciona o gerenciamento manual com `try ... finally` e `close()` antes de utilizar a abstração do `with`.

### P3: O que acontece se ocorrer um erro na linha `open()` dentro do `try`? Por que checar `if file_obj is not None:` no `finally`?
> **Resposta**: Se `open()` falhar (por exemplo, arquivo não existe), a atribuição `file_obj = open(...)` é interrompida imediatamente e o Python pula direto para o bloco `except`. Nesse cenário, `file_obj` continua com seu valor inicial (`None`). Se tentássemos chamar `file_obj.close()` sem verificar, o programa lançaria um `AttributeError: 'NoneType' object has no attribute 'close'`. A verificação garante que só tentamos fechar o que foi realmente aberto.

### P4: Como o statement `with` funciona por debaixo dos panos?
> **Resposta**: O `with` utiliza o protocolo de Context Manager, que exige dois métodos especiais:
> - `__enter__()`: Executado no início do bloco `with`. O valor que ele retorna é atribuído à variável do `as` (ex.: `as archive_file`).
> - `__exit__(exc_type, exc_val, exc_tb)`: Executado obrigatoriamente ao sair do bloco, quer ocorra erro ou não. No caso de arquivos, o `__exit__` chama automaticamente o método `.close()`.

### P5: Qual é a diferença técnica entre `sys.stdout` e `sys.stderr`?
> **Resposta**: Ambos são fluxos de saída padrão do sistema operacional, mas com propósitos e comportamentos de buffer diferentes:
> - `sys.stdout` é voltado para a saída normal do programa e geralmente possui buffer (*buffered*).
> - `sys.stderr` é dedicado a diagnósticos e mensagens de erro, permitindo separar logs de erros do fluxo de dados principal. Em pipelines Unix (`prog1 | prog2` ou `prog > out.txt`), o `stderr` continua sendo exibido no terminal, sem poluir os dados redirecionados do `stdout`.

---

## 6. Instruções de Execução e Testes

Para testar todos os exercícios individualmente:

### Exercício 0:
```bash
# Teste sem argumentos (deve exibir Usage):
python3 ex0/ft_ancient_text.py

# Teste com arquivo inexistente:
python3 ex0/ft_ancient_text.py foo

# Teste com arquivo válido:
echo "linha 1\nlinha 2" > test.txt
python3 ex0/ft_ancient_text.py test.txt
rm test.txt
```

### Exercício 1:
```bash
echo -e "Protocol 001\nProtocol 002" > test.txt

# Teste sem salvar (pressione Enter no prompt):
python3 ex1/ft_archive_creation.py test.txt

# Teste salvando em novo arquivo:
echo "output.txt" | python3 ex1/ft_archive_creation.py test.txt
cat output.txt
rm test.txt output.txt
```

### Exercício 2:
```bash
# Teste de erro no stderr:
python3 ex2/ft_stream_management.py arquivo_que_nao_existe

# Teste com arquivo válido redirecionando saída:
echo -e "Line A\nLine B" > test.txt
echo "new.txt" | python3 ex2/ft_stream_management.py test.txt
cat new.txt
rm test.txt new.txt
```

### Exercício 3:
```bash
# Executa a demonstração completa dos 4 casos de segurança:
python3 ex3/ft_vault_security.py
```

