from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """An extra ability, deliberately NOT a Creature."""

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
