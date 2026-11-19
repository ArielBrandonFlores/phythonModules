import importlib



def check_reagent(name: str, description: str) -> bool:
    try:
        module = importlib.import_module(name)
        version:str = getattr(module, "__version__", "Unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - Not installed ({description})")
        return False


def display_install_instructions() -> None:
    print("\nWARNING: Missing reagents detected!")
    print("To stock the laboratory using pip, run:")
    print("  pip install -r ex0/requirements.txt\n")
    print("To stock the laboratory using Poetry, run:")
    print("  poetry config virtualenvs.in-project true")
    print("  poetry install")
    print("  poetry run python ex0/loading.py")


def display_pip_vs_poetry() -> None:
    print("\npip vs Poetry:")
    print("  requirements.txt declares what to install; pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print("\nAll reagents present and accounted for.")


def main() -> None:
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    reagents: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
    ]

    all_present: bool = True
    for name, description in reagents:
        if not check_reagent(name, description):
            all_present = False

    if all_present:
        display_pip_vs_poetry()
    else:
        display_install_instructions()


if __name__ == "__main__":
    main()




