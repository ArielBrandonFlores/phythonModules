#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "a" + 1  # type: ignore
    else:
        pass # Não faz nada, a operação é bem sucedida

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    # O ciclo percorre de 0 até 4 para testar todas as condições
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            # Se a operação falhar, o código salta imediatamente para um dos 'except'.
            # Se não falhar (como no caso do 4), esta linha abaixo é executada:
            print("Operation completed successfully")

        except ValueError as erro:
            print(f"Caught ValueError: {erro}")
        except ZeroDivisionError as erro:
            print(f"Caught ZeroDivisionError: {erro}")
        except FileNotFoundError as erro:
            print(f"Caught FileNotFoundError: {erro}")
        except TypeError as erro:
            print(f"Caught TypeError: {erro}")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
