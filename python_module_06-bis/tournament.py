from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (AggressiveStrategy, BattleStrategy, InvalidStrategyError,
                 NormalStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponents]
    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                first, first_strategy = fighters[i]
                second, second_strategy = fighters[j]
                print("* Battle *")
                print(first.describe())
                print("vs.")
                print(second.describe())
                print("now fight!")
                first_strategy.act(first)
                second_strategy.act(second)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    tournaments: list[tuple[str, list[tuple[CreatureFactory,
                                            BattleStrategy]]]] = [
        ("basic", [(flame, normal), (transform, aggressive)]),
        ("error", [(transform, aggressive), (flame, aggressive)]),
    ]
    for index, (label, opponents) in enumerate(tournaments):
        print(f"Tournament {index} ({label})")
        names = [f"({factory.create_base().name}+{strategy.name})"
                 for factory, strategy in opponents]
        print("[ " + ", ".join(names) + " ]")
        battle(opponents)


if __name__ == "__main__":
    main()
