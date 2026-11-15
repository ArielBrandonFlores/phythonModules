import sys
import os
import site


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def display_open_lab() -> None:
    print("\nLABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def display_sealed_lab() -> None:
    env_path:str = sys.prefix
    env_name:str = os.path.basename(env_path)
    site_packages: list[str] = site.getsitepackages()
    reagent_path: str = site_packages[0]if site_packages else "Unknow"

    print("\nLABORATORY STATUS: The laboratory is sealed\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.\n")
    print("Reagent installation path:")
    print("/path/to/lab_env/lib/python3.11/site-packages")


def main() -> None:
    if is_virtual_environment():
        display_sealed_lab()
    else:
        display_open_lab()


if __name__ == "__main__":
    main()
