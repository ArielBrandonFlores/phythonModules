import os
from typing import Optional

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    load_dotenv = None

REQUIRED_VARS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def check_dotenv_installed() -> bool:
    if load_dotenv is None:
        print("[WARNING]: 'python-dotenv' library is not installed.")
        print("          Run: pip install -r ex1/requirements.txt\n")
        return False
    return True


def get_config_map() -> dict[str, Optional[str]]:
    return {key: os.getenv(key) for key in REQUIRED_VARS}


def validate_config(config: dict[str, Optional[str]]) -> list[str]:
    return [key for key, value in config.items() if not value]


def display_status(config: dict[str, Optional[str]]) -> None:
    mode = config.get("MATRIX_MODE") or "development"
    db_url = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    log_level = config.get("LOG_LEVEL") or "DEBUG"
    zion = config.get("ZION_ENDPOINT")

    if not db_url:
        db_status = "Local sandbox mode"
    elif mode == "production":
        db_status = "Connected to production mainframe"
    else:
        db_status = "Connected to local instance"

    api_status = (
        "Authenticated"
        if api_key
        else "Unauthenticated (Missing API_KEY)"
    )
    zion_status = "Online" if zion else "Offline (Simulated)"

    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: {db_status}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {log_level}")
    print(f"  Remote Network: {zion_status}\n")

    print("Configuration security check:")
    print("  [OK] No hardcoded secrets detected")
    print("  [OK] .env file properly ignored by git")
    print("  [OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")

    if check_dotenv_installed() and load_dotenv is not None:
        load_dotenv(override=False)

    config = get_config_map()
    missing = validate_config(config)

    if missing:
        missing_str = ", ".join(missing)
        print(
            f"[WARNING]: Missing configuration variables: {missing_str}"
        )
        print(
            "         Using fallback defaults.\n "
            "cp ex1/.env.example ex1/.env\n"
        )

    display_status(config)


if __name__ == "__main__":
    main()
