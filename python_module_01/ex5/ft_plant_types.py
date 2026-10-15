#!/usr/bin/env python3
class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days")

    def grow(self) -> None:
        self._height += 1.0

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    _color: str
    _is_blooming: bool

    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloommed yet!")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
        self, name: str, h: float, age: int, diam: float
    ) -> None:
        super().__init__(name, h, age)
        self._trunk_diameter = diam

    def produce_shade(self) -> None:
        h = round(self._height, 1)
        d = round(self._trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of {h}cm "
            f"long and {d}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{round(self._trunk_diameter, 1)}cm"
        )


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        season: str,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = season
        self._nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    print("=== Flower")
    rose = Flower("Rose", 10.0, 10, "red")
    rose.show()
    rose = Flower("Rose", 15.0, 10, "red")
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 47.0, 30, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
