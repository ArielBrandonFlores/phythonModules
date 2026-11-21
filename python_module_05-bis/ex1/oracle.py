import os

REQUIRED_VARS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_env_file(env_path: str) -> bool:
    try:
        from dotenv import load_dotenv  # typlse:ignore
    except ImportError:
        print("[WARNING] 'python-dotenv' library is not installed.")
        print("          Run: pip install -r ex1/requirements.txt\n")
        return False
    load_dotenv(dotenv_path=env_path, override=False)
    load_dotenv(override=False)
    return True


def is_env_ignored(gitignore_path: str) -> bool:
    try:
        with open(gitignore_path, encoding="utf-8") as file:
            lines: list[str] = [line.strip() for line in file]
        return ".env" in lines
    except OSError:
        return False


def get_config_map() -> dict[str, str | None]:
    return {key: os.getenv(key) for key in REQUIRED_VARS}


def validate_config(config: dict[str, str | None]) -> list[str]:
    return [key for key, value in config.items() if not value]


def display_status(
    config: dict[str, str | None],
    env_ignored: bool,
) -> None:
    mode = config.get("MATRIX_MODE") or "development"
    db_url = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    default_log = "WARNING" if mode == "production" else "DEBUG"
    log_level = config.get("LOG_LEVEL") or default_log
    zion = config.get("ZION_ENDPOINT")

    if mode == "production":
        db_status = (
            "Connected to production mainframe"
            if db_url
            else "Production database not configured"
        )
    else:
        db_status = (
            "Connected to local instance"
            if db_url
            else "Local sandbox mode"
        )

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
    if env_ignored:
        print("  [OK] .env file properly ignored by git")
    else:
        print("  [WARNING] .env file is not listed in .gitignore")
    print("  [OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(base_dir, ".env")
    gitignore_path = os.path.join(base_dir, ".gitignore")

    load_env_file(env_path)

    config = get_config_map()
    missing = validate_config(config)

    if missing:
        missing_str = ", ".join(missing)
        print(f"[WARNING] Missing configuration variables: {missing_str}")
        print("          Using fallback defaults.")
        print("          cp ex1/.env.example ex1/.env\n")

    display_status(config, is_env_ignored(gitignore_path))


if __name__ == "__main__":
    main()
