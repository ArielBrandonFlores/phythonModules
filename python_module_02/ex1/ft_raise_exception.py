#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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

    temperature_hot = "100"
    print(f"Input data is '{temperature_hot}'")
    try:
        print(f"Temperature is now {input_temperature(temperature_hot)}°C\n")
    except ValueError as erro:
        print(f"Caught input_temperature error: {erro}\n")

    temperature_cold = "-50"
    print(f"Input data is '{temperature_cold}'")
    try:
        print(f"Temperature is now {input_temperature(temperature_cold)}°C\n")
    except ValueError as erro:
        print(f"Caught input_temperature error: {erro}\n")


if __name__ == "__main__":
    test_temperature()
