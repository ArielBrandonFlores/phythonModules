#!/usr/bin/env python3
import random


ACHIEVEMENTS_POOL: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
    "Unstoppable"
]


def gen_player_achievements() -> set[str]:
    num_achievements: int = random.randint(5, 9)
    selected: list[str] = random.sample(ACHIEVEMENTS_POOL, num_achievements)

    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    for name, achievements in players:
        print(f"Player {name}: {achievements}")

    player_sets: list[set[str]] = []
    for name, achievements in players:
        player_sets.append(achievements)

    all_distinct: set[str] = set.union(*player_sets)
    print(f"All distinct achievements: {all_distinct}")

    common_achievements: set[str] = set.intersection(*player_sets)
    print(f"Common achievements: {common_achievements}")

    for name, current_set in players:
        other_sets: list[set[str]] = []
        for other_name, other_set in players:
            if other_name != name:
                other_sets.append(other_set)

        other_union: set[str] = set.union(*other_sets)
        unique_to_player: set[str] = set.difference(current_set, other_union)
        print(f"Only {name} has: {unique_to_player}")

    all_possible: set[str] = set(ACHIEVEMENTS_POOL)
    for name, current_set in players:
        missing_achievements: set[str] = set.difference(
            all_possible, current_set
        )
        print(f"{name} is missing: {missing_achievements}")


if __name__ == "__main__":
    main()
