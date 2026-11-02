import sys
import typing


def recover_ancient_text(filename: str) -> None:
    """Read and display the contents of an archive file safely without with."""
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content: str = file_obj.read()
        print("---")
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)
        print("---")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")


def main() -> None:
    """Validate command line arguments and execute text recovery."""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()

