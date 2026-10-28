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

def simulate_plant_issue() -> None:
    raise PlantError("The tomato plant is wilting!")

def simulate_water_issue() -> None:
    raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
    print("Custom Garden Errors Demo")

    print("Testing PlantError...")
    try:
        simulate_plant_issue()
    except PlantError as erro:
        print(f"Caught PlantError: {erro}")

    print("Testing WaterError...")
    try:
        simulate_water_issue()
    except WaterError as erro:
        print(f"Caught WaterError: {erro}")

    # Nota: A string abaixo tem dois pontos finais ("..") para igualar o PDF
    print("Testing catching all garden errors..")

    # Demonstração de captura genérica: PlantError é apanhado pelo seu "pai" GardenError
    try:
        simulate_plant_issue()
    except GardenError as erro:
        print(f"Caught GardenError: {erro}")

    # WaterError também é apanhado pelo "pai" GardenError
    try:
        simulate_water_issue()
    except GardenError as erro:
        print(f"Caught GardenError: {erro}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
