#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    temperature_val = "25"
    print(f"Input data is '{temperature_val}'")
    try:
        print(f"Temperature is now {input_temperature(temperature_val)}°C\n")
    except ValueError as erro:
        print(f"Caught input_temperature error: {erro}\n")

    temperature_inv = "abc"
    print(f"Input data is '{temperature_inv}'")
    try:
        print(f"Temperature is now {input_temperature(temperature_inv)}°C\n")
    except ValueError as erro:
        print(f"Caught input_temperature error: {erro}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
