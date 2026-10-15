#!/usr/bin/env python3
class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show",
                end="",
            )

    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = self.Statistics()

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.set_height(self._height + 8.0)
        self._stats.increment_grow()

    def age(self) -> None:
        self.set_age(self._age + 20)
        self._stats.increment_age()

    def show(self) -> None:
        h = round(self._height, 1)
        print(f"{self._name}: {h}cm, {self._age} days old")
        self._stats.increment_show()


class Flower(Plant):
    _color: str
    _is_blooming: bool

    def __init__(
        self,
        name: str,
        h: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, h, age)
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
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):

    _seeds: int

    def __init__(
        self,
        name: str,
        h: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, h, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self, name: str) -> None:
            super().display(name)
            print(f" {self._shade_calls} shade")

    _trunk_diameter: float
    _stats: TreeStatistics

    def __init__(
        self,
        name: str,
        h: float,
        age: int,
        diam: float,
    ) -> None:
        super().__init__(name, h, age)
        self._trunk_diameter = diam
        self._stats: Tree.TreeStatistics = self.TreeStatistics()

    def produce_shade(self) -> None:
        self._stats.increment_shade()
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


def display_plant_stats(plant: Plant) -> None:
    plant._stats.display(plant._name)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("\n=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("\n[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    print("\n[make sunflower grow, age and bloom]")
    sun.grow()
    sun.age()
    sun.bloom()
    sun.show()
    display_plant_stats(sun)

    print("\n\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
