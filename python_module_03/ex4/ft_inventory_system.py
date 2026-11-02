#!/usr/bin/env python3
import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    """Parse item:quantity arguments into an inventory dictionary."""
    inventory: dict[str, int] = {}

    for argument in arguments:
        parts: list[str] = argument.split(":")
        
        # Validação estrita de formato exigida pelo PDF (exatamente um ':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name: str = parts[0]
        quantity_str: str = parts[1]

        # Verifica redundância
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        # Tenta converter a quantidade e captura o erro do ValueError
        try:
            quantity: int = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as error:
            # Imprime o erro nativo do Python interpolado na string
            print(f"Quantity error for '{item_name}': {error}")

    return inventory


def display_analytics(inventory: dict[str, int]) -> None:
    """Calculate and display statistics for the given inventory."""
    print(f"Got inventory: {inventory}")

    # Uso obrigatório de dict.keys() e list()
    item_names: list[str] = list(inventory.keys())
    print(f"Item list: {item_names}")

    # Uso obrigatório de dict.values() e sum()
    total_quantity: int = sum(inventory.values())
    total_items: int = len(inventory)
    print(f"Total quantity of the {total_items} items: {total_quantity}")

    # Evita divisão por zero e processa as porcentagens
    if total_quantity > 0:
        for item_name, quantity in inventory.items():
            percentage: float = round((quantity / total_quantity) * 100, 1)
            print(f"Item {item_name} represents {percentage}%")

        # Variáveis para rastrear os mais e menos abundantes
        most_item: str = item_names[0]
        most_qty: int = inventory[most_item]
        least_item: str = item_names[0]
        least_qty: int = inventory[least_item]

        for item_name, quantity in inventory.items():
            # Operadores estritos (>) e (<) garantem que em caso de empate,
            # o primeiro item inserido (e lido) é mantido.
            if quantity > most_qty:
                most_qty = quantity
                most_item = item_name

            if quantity < least_qty:
                least_qty = quantity
                least_item = item_name

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

    # Uso obrigatório de dict.update()
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    
    # Se não houver argumentos (inventário vazio no começo do jogo)
    raw_args: list[str] = sys.argv[1:]
    if not raw_args:
        # Apenas imprime as etapas em branco para evitar erros,
        # ou encerra silenciosamente após o título, se preferir.
        return

    inventory: dict[str, int] = parse_inventory(raw_args)
    
    if inventory:
        display_analytics(inventory)


if __name__ == "__main__":
    main()