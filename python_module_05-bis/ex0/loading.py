#!/usr/bin/env python3
"""Stocking the reagents: check that the declared dependencies are present."""

import importlib
import os
import sys


REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
}


def load_reagent(name: str) -> str | None:
    """Import a reagent by name and return its version, or None if missing."""
    try:
        module: object = importlib.import_module(name)
    except ImportError:
        return None
    return str(getattr(module, "__version__", "unknown version"))


def describe_environment() -> None:
    """Tell where the reagents are being looked for."""
    if "pypoetry" in sys.prefix or os.environ.get("POETRY_ACTIVE"):
        manager = "Poetry managed environment"
    elif sys.prefix != sys.base_prefix:
        manager = "virtual environment"
    else:
        manager = "global environment"
    print(f"Environment: {manager} ({sys.prefix})")


def explain_pip_vs_poetry() -> None:
    """Print the difference between pip and Poetry."""
    print("pip vs Poetry:")
    print(" requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print(" pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print(" versions in poetry.lock so every install is identical.")


def print_install_help(missing: list[str]) -> None:
    """Print how to install the missing reagents with pip and Poetry."""
    folder = os.path.relpath(os.path.dirname(os.path.abspath(__file__)))
    requirements = os.path.join(folder, "requirements.txt")
    names = " ".join(missing)
    print("Missing reagents! Install them with one of the following:")
    print(" With pip:")
    print(f"   pip install -r {requirements}")
    print(f"   (or: pip install {names})")
    print(" With Poetry:")
    print(f"   cd {folder} && poetry install")
    print(f"   (or: poetry add {names})")
    print("   then run: poetry run python loading.py")


def main() -> None:
    """Entry point."""
    print("REAGENT STATUS: Loading reagents...")
    describe_environment()
    print()
    print("Checking dependencies:")
    missing: list[str] = []
    for name, role in REAGENTS.items():
        version = load_reagent(name)
        if version is None:
            missing.append(name)
            print(f"[MISSING] {name} - {role} unavailable")
        else:
            print(f"[OK] {name} ({version}) - {role} ready")
    print()
    explain_pip_vs_poetry()
    print()
    if missing:
        print_install_help(missing)
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
