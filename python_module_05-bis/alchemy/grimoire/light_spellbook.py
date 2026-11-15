"""Light spellbook: knows the allowed ingredients and records spells."""
from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a spell if the validator accepts its ingredients."""
    verdict = validate_ingredients(ingredients)
    if verdict.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({verdict})"
    return f"Spell rejected: {spell_name} ({verdict})"
