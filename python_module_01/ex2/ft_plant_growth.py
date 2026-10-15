#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def age_up(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height += 0.8

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


if __name__ == "__main__":

    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)

    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_up()
        rose.show()

    total_growth = rose.height - initial_height
    print(f"Growth this week: {round(total_growth, 1)}cm")
