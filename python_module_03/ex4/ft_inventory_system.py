#!/usr/bin/env python3
import sys


def parse_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for argument in arguments:
        parts: list[str] = argument.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name: str = parts[0]
        quantity_str: str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            inventory[item_name] = int(quantity_str)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")

    return inventory


def display_analytics(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")

    item_names: list[str] = list(inventory.keys())
    print(f"Item list: {item_names}")

    total_quantity: int = sum(inventory.values())
    total_items: int = len(inventory)
    print(f"Total quantity of the {total_items} items: {total_quantity}")

    if total_quantity > 0:
        for item_name in inventory.keys():
            quantity = inventory[item_name]
            percentage: float = round((quantity / total_quantity) * 100, 1)
            print(f"Item {item_name} represents {percentage}%")

        most_item: str = item_names[0]
        most_qty: int = inventory[most_item]
        least_item: str = item_names[0]
        least_qty: int = inventory[least_item]

        for item_name in inventory.keys():
            quantity = inventory[item_name]
            if quantity > most_qty:
                most_qty = quantity
                most_item = item_name

            if quantity < least_qty:
                least_qty = quantity
                least_item = item_name

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    raw_args: list[str] = sys.argv[1:]
    if not raw_args:
        return

    inventory: dict[str, int] = parse_inventory(raw_args)

    if inventory:
        display_analytics(inventory)


if __name__ == "__main__":
    main()
