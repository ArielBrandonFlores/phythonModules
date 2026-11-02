import sys
import typing


def transform_data(content: str) -> str:
    """Append the '#' character to the end of each line."""
    lines: list[str] = content.splitlines()
    if not lines:
        return ""
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed_lines) + "\n"


def save_archive_data(filename: str, content: str) -> None:
    """Save content to target file without using with statement."""
    print(f"Saving data to '{filename}'")
    out_file: typing.IO[str] | None = None
    try:
        out_file = open(filename, "w")
        out_file.write(content)
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        print(f"Error saving to '{filename}': {error}")
    finally:
        if out_file is not None:
            out_file.close()


def recover_and_preserve(filename: str) -> None:
    """Read, display, transform, and optionally save archive data."""
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    raw_content: str | None = None

    try:
        file_obj = open(filename, "r")
        raw_content = file_obj.read()
        print("---")
        if raw_content.endswith("\n"):
            print(raw_content, end="")
        else:
            print(raw_content)
        print("---")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")

    if raw_content is None:
        return

    print("\nTransform data:")
    print("---")
    transformed_content: str = transform_data(raw_content)
    if transformed_content.endswith("\n"):
        print(transformed_content, end="")
    else:
        print(transformed_content)
    print("---")

    new_filename: str = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    save_archive_data(new_filename, transformed_content)


def main() -> None:
    """Validate arguments and start preservation pipeline."""
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    recover_and_preserve(sys.argv[1])


if __name__ == "__main__":
    main()

