#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts: list[str] = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        valid: bool = True
        coordinates: list[float] = []
        for part in parts:
            clean_part: str = part.strip()
            try:
                coordinates.append(float(clean_part))
            except ValueError as error:
                print(f"Error on parameter '{clean_part}': {error}")
                valid = False
                break
        if valid:
            return (coordinates[0], coordinates[1], coordinates[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center: float = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist_between: float = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(
        f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}"
        )


if __name__ == "__main__":
    main()
