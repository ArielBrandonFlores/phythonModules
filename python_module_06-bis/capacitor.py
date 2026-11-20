from ex3 import TransformCreatureFactory
from ex3.capability import TransformCapability
from ex3.creature import Creature


def test_transform(label: str, creature: Creature) -> None:
    print(f"{label}:")
    print(creature.describe())
    print(creature.attack())
    if not isinstance(creature, TransformCapability):
        print(f"{creature.name} can't transform.")
        return
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    test_transform("base", factory.create_base())
    test_transform("evolved", factory.create_evolved())


if __name__ == "__main__":
    main()
