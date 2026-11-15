#!/usr/bin/env python3
"""The Oracle: a configuration system based on environment variables."""

import os
import sys


HERE: str = os.path.dirname(os.path.abspath(__file__))
ENV_FILE: str = os.path.join(HERE, ".env")
GITIGNORE_FILE: str = os.path.join(HERE, ".gitignore")

CONFIG_KEYS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]
SECRET_KEYS: list[str] = ["DATABASE_URL", "API_KEY"]
VALID_MODES: list[str] = ["development", "production"]
DEFAULT_LOG_LEVEL: dict[str, str] = {
    "development": "DEBUG",
    "production": "WARNING",
}


def load_env_file() -> bool:
    """Load ex1/.env without overriding variables already in the environment.

    Returns True if a .env file was found and loaded.
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("[WARNING] python-dotenv is not installed, .env file ignored")
        print("          pip install -r ex1/requirements.txt")
        return False
    if not os.path.isfile(ENV_FILE):
        return False
    return load_dotenv(ENV_FILE, override=False)


def read_config() -> tuple[dict[str, str | None], dict[str, str]]:
    """Read the configuration and remember where each value comes from."""
    from_environment = {key for key in CONFIG_KEYS if key in os.environ}
    load_env_file()
    config: dict[str, str | None] = {}
    sources: dict[str, str] = {}
    for key in CONFIG_KEYS:
        value = os.environ.get(key)
        config[key] = value if value else None
        if not value:
            sources[key] = "default"
        elif key in from_environment:
            sources[key] = "environment"
        else:
            sources[key] = ".env file"
    return config, sources


def mask(value: str, production: bool) -> str:
    """Hide a secret, revealing a small hint only in development."""
    if production or len(value) <= 4:
        return "********"
    return value[:3] + "*" * (len(value) - 3)


def describe_database(url: str | None, production: bool) -> str:
    """Describe the database connection."""
    if url is None:
        return "Not configured (using in-memory fallback)"
    if production:
        return "Connected to production cluster"
    return "Connected to local instance"


def describe_api(key: str | None) -> str:
    """Describe the API access."""
    if key is None:
        return "Unauthenticated (no API_KEY)"
    return "Authenticated"


def describe_network(endpoint: str | None) -> str:
    """Describe the remote network status."""
    if endpoint is None:
        return "Offline (no ZION_ENDPOINT)"
    return "Online"


def source_has_secret(config: dict[str, str | None]) -> bool:
    """Check whether a configured secret is written in this very file."""
    try:
        with open(os.path.abspath(__file__), "r") as source_file:
            source = source_file.read()
    except OSError:
        return False
    for key in SECRET_KEYS:
        value = config[key]
        if value is not None and len(value) > 4 and value in source:
            return True
    return False


def env_file_ignored() -> bool:
    """Check that .env is listed in ex1/.gitignore."""
    try:
        with open(GITIGNORE_FILE, "r") as gitignore:
            lines = [line.strip() for line in gitignore]
    except OSError:
        return False
    return ".env" in lines or "*.env" in lines


def security_check(config: dict[str, str | None],
                   sources: dict[str, str]) -> None:
    """Print the configuration security report."""
    print("Configuration security check:")
    if source_has_secret(config):
        print("[WARNING] A secret is hardcoded in the source code!")
    else:
        print("[OK] No hardcoded secrets detected")
    if env_file_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file is NOT listed in ex1/.gitignore!")
    overridden = [key for key in CONFIG_KEYS
                  if sources[key] == "environment"]
    if overridden:
        print("[OK] Production overrides available "
              f"(from environment: {', '.join(overridden)})")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    """Entry point."""
    print("ORACLE STATUS: Consulting the configuration...")
    config, sources = read_config()

    missing = [key for key in CONFIG_KEYS if config[key] is None]
    mode = config["MATRIX_MODE"] or "development"
    if mode not in VALID_MODES:
        print(f"[WARNING] Unknown MATRIX_MODE '{mode}', "
              "falling back to development")
        mode = "development"
    production = mode == "production"
    log_level = config["LOG_LEVEL"] or DEFAULT_LOG_LEVEL[mode]

    if missing:
        print()
        print("[WARNING] Missing configuration: " + ", ".join(missing))
        if not os.path.isfile(ENV_FILE):
            print("          No .env file found, try: "
                  "cp ex1/.env.example ex1/.env")
        print("          Default values will be used.")

    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    database = describe_database(config["DATABASE_URL"], production)
    print(f"Database: {database}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {describe_network(config['ZION_ENDPOINT'])}")

    print()
    if production:
        print("Production mode: details hidden, secrets fully masked.")
        critical = [key for key in SECRET_KEYS if config[key] is None]
        if critical:
            print("[ERROR] Production requires: " + ", ".join(critical))
    else:
        print("Development details (never shown in production):")
        for key in CONFIG_KEYS:
            value = config[key]
            if value is None:
                shown = "<unset>"
            elif key in SECRET_KEYS:
                shown = mask(value, production)
            else:
                shown = value
            print(f"  {key:<14} = {shown:<30} [{sources[key]}]")

    print()
    security_check(config, sources)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
