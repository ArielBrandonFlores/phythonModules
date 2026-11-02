#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    # A lista inicial de jogadores baseada no exemplo do PDF
    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    # List comprehension 1: Retorna uma nova lista com todos os nomes capitalizados
    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    # List comprehension 2: Filtra apenas os nomes que já começavam com maiúscula
    # O método .istitle() é perfeito para verificar palavras como "Alice"
    only_capitalized: list[str] = [name for name in players if name.istitle()]
    print(f"New list of capitalized names only: {only_capitalized}")

    # Dict comprehension 1: Mapeia a lista capitalizada gerando scores aleatórios
    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    # Cálculo seguro da média (garantido pelo PDF que o len > 0)
    average_score: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average_score}")

    # Dict comprehension 2: Filtra e mapeia apenas quem ficou acima da média
    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()