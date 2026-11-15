"""Transmutation recipes."""

# Absolute imports: full path starting from the project root
from elements import create_fire
from alchemy.elements import create_air
# Relative import: '..' climbs from alchemy.transmutation up to alchemy
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Transmute lead into gold."""
    return ("Recipe transmuting Lead to Gold: "
            f"brew '{create_air()}' and '{strength_potion()}' "
            f"mixed with '{create_fire()}'")
