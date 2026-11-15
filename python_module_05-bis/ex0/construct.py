#!/usr/bin/env python3
"""The Sealed Laboratory: detect and describe the Python environment."""

import os
import sys
import site


def is_sealed() -> bool:
    """Return True when running inside a virtual environment.

    Inside a venv, sys.prefix points to the venv directory while
    sys.base_prefix still points to the Python installation it was
    created from. Outside a venv, both are identical.
    """
    return sys.prefix != sys.base_prefix


def existing(locations: list[str]) -> list[str]:
    """Keep only the directories that really exist on disk."""
    found = [path for path in locations if os.path.isdir(path)]
    return found if found else locations


def global_package_locations() -> list[str]:
    """Return the site-packages directories of the global installation."""
    return existing(site.getsitepackages([sys.base_prefix]))


def local_package_locations() -> list[str]:
    """Return the site-packages directories of the current environment."""
    return existing(site.getsitepackages([sys.prefix]))


def print_locations(title: str, locations: list[str]) -> None:
    """Print a titled list of directories."""
    print(title)
    for location in locations:
        print(f"  {location}")


def open_laboratory() -> None:
    """Report for a program running in the global environment."""
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print_locations("Global reagent installation path(s):",
                    global_package_locations())
    print()
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate  # On Unix")
    print("lab_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")


def sealed_laboratory() -> None:
    """Report for a program running inside a virtual environment."""
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")
    print()
    print_locations("Reagent installation path:", local_package_locations())
    print()
    print_locations("Global reagent path (outside the seal, not used):",
                    global_package_locations())


def main() -> None:
    """Entry point."""
    if is_sealed():
        sealed_laboratory()
    else:
        open_laboratory()


if __name__ == "__main__":
    main()
