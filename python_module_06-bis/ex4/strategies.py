from abc import ABC, abstractmethod

from ex3.capability import TransformCapability
from ex3.creature import Creature


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with a creature it does not fit."""


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    def _invalid(self, creature: Creature) -> InvalidStrategyError:
        return InvalidStrategyError(
            f"Invalid Creature '{creature.name}' "
            f"for this {self.name.lower()} strategy"
        )


class NormalStrategy(BattleStrategy):
    name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise self._invalid(creature)
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise self._invalid(creature)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
