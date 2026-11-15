# Diretrizes e Regras do Projeto - Data Archivist (Python Module 04)

Este documento estabelece as regras e especificações do projeto **Data Archivist: Digital Preservation in the Cyber Archives (Version 3.0)** extraídas diretamente do subject (`en.subject_python4.pdf`). Estas diretrizes **devem ser estritamente obedecidas** em todas as implementações deste repositório.

---

## 1. Regras Comuns e Padrões Globais

### 1.1 Versão e Qualidade de Código
- **Versão do Python**: Todos os programas devem ser escritos para **Python 3.10 ou superior**.
- **Conformidade com Linter**: O código deve passar 100% sem erros ou avisos na validação com `flake8`.
- **Tipagem Estática (Type Hints)**: Todas as funções e métodos **devem** incluir anotações de tipo completas (`type hints`), verificáveis sem erros via `mypy`.
- **Tratamento de Exceções**: Todas as funções devem tratar exceções de forma graciosa para evitar travamentos (*crashes* não tratados / tracebacks não capturados).
- **Tipos e Coleções Permitidos**: Apenas os seguintes tipos e coleções padrão (e seus métodos/construtores associados) são permitidos:
  - `str`
  - `int`
  - `float`
  - `list`
  - `dict`
  - `set`
  - `tuple`

### 1.2 Regra Fundamental do Context Manager (`with`)
> [!CAUTION]
> **O uso da instrução `with` (context manager) é expressamente PROIBIDO nos Exercícios 0, 1 e 2.**
> O statement `with` só é introduzido e permitido no **Exercício 3**.
> Nos exercícios 0, 1 e 2, o gerenciamento de arquivos deve ser feito manualmente utilizando `open()`, `close()` e blocos `try ... except ... finally`.

---

## 2. Especificação dos Exercícios

### Exercício 0: Ancient Text Recovery
- **Diretório**: `ex0/`
- **Arquivo a submeter**: `ft_ancient_text.py`
- **Elementos Autorizados**:
  `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.close()`, `print()`
- **Proibições**:
  - Proibido usar a instrução `with`.
- **Objetivo e Comportamento**:
  1. Obter o nome do arquivo a partir dos argumentos da linha de comando (`sys.argv`).
  2. Se a quantidade de argumentos for incorreta, exibir a mensagem de uso e encerrar:
     ```text
     Usage: ft_ancient_text.py <file>
     ```
  3. Exibir o cabeçalho:
     ```text
     === Cyber Archives Recovery ===
     Accessing file '<file>'
     ```
  4. Tratar possíveis erros na abertura/leitura do arquivo (ex.: arquivo não encontrado, sem permissão de leitura):
     ```text
     Error opening file '<file>': [Errno 2] No such file or directory: '<file>'
     ```
  5. Se o arquivo for lido com sucesso:
     - Imprimir o separador `---`
     - Imprimir o conteúdo do arquivo
     - Imprimir o separador `---`
     - Fechar o arquivo explicitamente
     - Imprimir:
       ```text
       File '<file>' closed.
       ```

---

### Exercício 1: Archive Creation
- **Diretório**: `ex1/`
- **Arquivo a submeter**: `ft_archive_creation.py`
- **Elementos Autorizados**:
  `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.write()`, `io.close()`, `print()`, `input()`
- **Proibições**:
  - Proibido usar a instrução `with`.
- **Objetivo e Comportamento**:
  1. Basear-se no código do Exercício 0 com cabeçalho atualizado:
     ```text
     === Cyber Archives Recovery & Preservation ===
     ```
  2. Ler e exibir o conteúdo do arquivo original conforme o Exercício 0 e fechar o arquivo original.
  3. Aplicar transformação aos dados:
     - Adicionar o caractere `#` ao final de cada linha lida.
     - Exibir a seção de dados transformados:
       ```text
       Transform data:
       ---
       <linhas com # no final>
       ---
       ```
  4. Solicitar ao usuário o nome do novo arquivo para salvar usando `input()`:
     ```text
     Enter new file name (or empty): 
     ```
  5. Se o usuário fornecer uma entrada vazia:
     ```text
     Not saving data.
     ```
  6. Se o usuário fornecer um nome de arquivo:
     - Exibir: `Saving data to '<filename>'`
     - Gravar o conteúdo transformado no arquivo (criando ou substituindo caso já exista).
     - Fechar o arquivo de escrita.
     - Exibir: `Data saved in file '<filename>'.`
  7. Tratar exceções de I/O adequadamente.

---

### Exercício 2: Stream Management
- **Diretório**: `ex2/`
- **Arquivo a submeter**: `ft_stream_management.py`
- **Elementos Autorizados**:
  `import sys`, `sys.argv`, `sys.stdin`, `sys.stdout`, `sys.stderr`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.readline()`, `io.write()`, `io.flush()`, `io.close()`, `print()`
- **Proibições**:
  - Proibido usar a instrução `with`.
  - **Proibido usar a função built-in `input()`**. A entrada do usuário deve ser obtida via fluxos (`sys.stdin.readline()`).
- **Objetivo e Comportamento**:
  1. Atualizar o programa do Exercício 1 para gerenciar adequadamente os fluxos padrão (`sys.stdin`, `sys.stdout`, `sys.stderr`).
  2. Redirecionar **mensagens de erro decorrentes de exceções** para a saída padrão de erro (`sys.stderr`), adicionando o prefixo `[STDERR]`:
     ```text
     [STDERR] Error opening file '<file>': <detalhes do erro>
     ```
  3. Solicitar e ler a entrada do usuário através de `sys.stdin` (e `sys.stdout` para o prompt).
  4. Em caso de falha na gravação do novo arquivo:
     - Emitir mensagem no `sys.stderr` com prefixo `[STDERR]`.
     - Exibir na saída padrão (`sys.stdout`): `Data not saved.`

---

### Exercício 3: Vault Security
- **Diretório**: `ex3/`
- **Arquivo a submeter**: `ft_vault_security.py`
- **Elementos Autorizados**:
  `open()`, `read()`, `write()`, `print()` (mais tipos permitidos e anotações de tipo)
- **Obrigatoriedades**:
  - **Uso OBRIGATÓRIO da instrução `with`** (context manager) para garantir liberação segura de recursos.
- **Objetivo e Comportamento**:
  1. Implementar a função:
     ```python
     def secure_archive(
         filename: str,
         action: str | int = "read",
         content: str | None = None
     ) -> tuple[bool, str]:
     ```
  2. A função deve fornecer acesso seguro a qualquer arquivo para leitura ou escrita:
     - Parâmetro 1: Nome do arquivo (`str`, obrigatório).
     - Parâmetro 2: Ação a ser executada (`str` ou `int`, opcional; ex.: leitura ou escrita).
     - Parâmetro 3: Conteúdo a escrever (`str`, opcional).
  3. Retorno:
     - Tupla `(True, <conteúdo do arquivo>)` se leitura com sucesso.
     - Tupla `(True, "Content successfully written to file")` se escrita com sucesso.
     - Tupla `(False, "<mensagem de erro>")` caso ocorra qualquer exceção.
  4. Bloco de execução principal (`__main__`):
     - Demonstrar testes correspondentes aos exemplos do subject:
       - Leitura de arquivo inexistente: `(False, "[Errno 2] No such file or directory: ...")`
       - Leitura de arquivo inacessível: `(False, "[Errno 13] Permission denied: ...")`
       - Leitura de arquivo regular: `(True, '<conteúdo>\\n...')`
       - Escrita de conteúdo em novo arquivo: `(True, 'Content successfully written to file')`

---

## 3. Entregas e Git

- Apenas os seguintes arquivos devem ser submetidos ao repositório remoto:
  - `ex0/ft_ancient_text.py`
  - `ex1/ft_archive_creation.py`
  - `ex2/ft_stream_management.py`
  - `ex3/ft_vault_security.py`
- Arquivos de teste, documentos do subject (`*.pdf`), saídas temporárias, caches (`__pycache__`, `.mypy_cache`) e quaisquer outros arquivos **NÃO** devem constar no repositório remoto.

