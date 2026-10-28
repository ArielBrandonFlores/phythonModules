#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/")
    elif operation_number == 3:
        "a" + 1
    else:
        pass


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")

        except ValueError as erro:
            print(f"Caught ValueError: {erro}")
        except ZeroDivisionError as erro:
            print(f"Caught ZeroDivisionError: {erro}")
        except FileNotFoundError as erro:
            print(f"Caught FileNotFoundError: {erro}")
        except TypeError as erro:
            print(f"Caught TypeError: {erro}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
