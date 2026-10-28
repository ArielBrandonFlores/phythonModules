#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water(tank_empty: bool) -> None:
    if tank_empty:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant(True)
    except PlantError as erro:
        print(f"Caught PlantError: {erro}")

    print("\nTesting WaterError...")
    try:
        check_water(True)
    except WaterError as erro:
        print(f"Caught WaterError: {erro}")

    print("\nTesting catching all garden errors..")

    try:
        check_plant(True)
    except GardenError as erro:
        print(f"Caught GardenError: {erro}")

    try:
        check_water(True)
    except GardenError as erro:
        print(f"Caught GardenError: {erro}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
