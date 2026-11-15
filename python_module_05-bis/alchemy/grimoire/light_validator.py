"""Light validator: checks ingredients against the light spellbook."""


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID.

    The spellbook imports this module at its top, so this module must not
    import the spellbook at its own top: the import is deferred until the
    function is actually called. By then, the spellbook module is fully
    initialised and light_spell_allowed_ingredients exists.
    """
    from .light_spellbook import light_spell_allowed_ingredients

    lowered = ingredients.lower()
    for allowed in light_spell_allowed_ingredients():
        if allowed in lowered:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
