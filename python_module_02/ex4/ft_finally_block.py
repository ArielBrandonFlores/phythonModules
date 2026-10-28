#!/usr/bin/env python3

# Reutilizamos a classe do exercício anterior como base
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    # Compara o nome original com a versão capitalizada
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    # --- Primeiro Teste: Plantas Válidas ---
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as erro:
        print(f"Caught PlantError: {erro}")
        print("ending tests and returning to main")
        return
    finally:
        # Isto é sempre executado
        print("Closing watering system\n")

    # --- Segundo Teste: Plantas Inválidas ---
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce") # Isto vai causar a falha
        water_plant("Carrots") # Isto nunca chegará a ser executado
    except PlantError as erro:
        print(f"Caught PlantError: {erro}")
        print("ending tests and returning to main")
        # O return força a saída imediata da função
        return
    finally:
        # Magia do Python: O finally é executado ANTES do return de cima se concretizar!
        print("Closing watering system\n")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
