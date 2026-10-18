#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = float(height)
        self._age: int = age

    def get_height(self) -> float:
        return self._height

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height += 0.8

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)

    initial_height: float = rose.get_height()
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    total_growth: float = rose.get_height() - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")
