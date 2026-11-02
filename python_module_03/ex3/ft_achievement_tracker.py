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
    """Seleciona aleatoriamente um conjunto de conquistas para o jogador."""
    # Garante a probabilidade de interseções e diferenças pedidas no PDF
    num_achievements: int = random.randint(5, 9)
    selected: list[str] = random.sample(ACHIEVEMENTS_POOL, num_achievements)
    
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===")

    # Usando lista de tuplas em vez de dict, pois dicionários pertencem ao ex04
    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]

    for name, achievements in players:
        print(f"Player {name}: {achievements}")

    # Extrai apenas os sets (conjuntos) para as operações matemáticas
    player_sets: list[set[str]] = []
    for _, achievements in players:
        player_sets.append(achievements)

    # 1. Track unique achievements among all players
    all_distinct: set[str] = set.union(*player_sets)
    print(f"All distinct achievements: {all_distinct}")

    # 2. Find achievements shared by all players
    common_achievements: set[str] = set.intersection(*player_sets)
    print(f"Common achievements: {common_achievements}")

    # 3. For each player, spot the achievements no one else has
    for name, current_set in players:
        # Pega os sets de todos os OUTROS jogadores
        other_sets: list[set[str]] = []
        for other_name, other_set in players:
            if other_name != name:
                other_sets.append(other_set)
                
        other_union: set[str] = set.union(*other_sets)
        
        # A diferença entre o set atual e a união de todos os outros
        unique_to_player: set[str] = set.difference(current_set, other_union)
        print(f"Only {name} has: {unique_to_player}")

    # 4. For each player, list the missing achievements to have them all
    all_possible: set[str] = set(ACHIEVEMENTS_POOL)
    for name, current_set in players:
        missing_achievements: set[str] = set.difference(all_possible, current_set)
        print(f"{name} is missing: {missing_achievements}")


if __name__ == "__main__":
    main()