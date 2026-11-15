"""Dark validator: checks ingredients against the dark spellbook."""
from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID.

    Naive design, on purpose: the spellbook is imported at the top of this
    module while the spellbook imports this module at its own top. Whoever
    is imported first is still half-built when the other one asks for its
    names, so the import cycle explodes before this function ever runs.
    """
    lowered = ingredients.lower()
    for allowed in dark_spell_allowed_ingredients():
        if allowed in lowered:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
