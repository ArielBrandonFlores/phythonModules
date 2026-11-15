"""Dark spellbook: knows the dark ingredients and records dark spells."""
from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell if the dark validator accepts its ingredients."""
    verdict = dark_validate_ingredients(ingredients)
    if verdict.endswith(" - VALID"):
        return f"Dark spell recorded: {spell_name} ({verdict})"
    return f"Dark spell rejected: {spell_name} ({verdict})"
