import sys
import typing


def transform_data(content: str) -> str:
    """Append the '#' character to the end of each line."""
    lines: list[str] = content.splitlines()
    if not lines:
        return ""
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed_lines) + "\n"


def read_user_input(prompt: str) -> str:
    """Prompt user and read one line from sys.stdin without using input()."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    if line.endswith("\r\n"):
        return line[:-2]
    if line.endswith("\n"):
        return line[:-1]
    return line


def save_archive_data(filename: str, content: str) -> None:
    """Save content to target file using streams for errors without with."""
    print(f"Saving data to '{filename}'")
    out_file: typing.IO[str] | None = None
    try:
        out_file = open(filename, "w")
        out_file.write(content)
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr,
        )
        print("Data not saved.")
    finally:
        if out_file is not None:
            out_file.close()


def recover_and_preserve(filename: str) -> None:
    """Execute recovery and preservation pipeline utilizing custom streams."""
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
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr,
        )
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

    new_filename: str = read_user_input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    save_archive_data(new_filename, transformed_content)


def main() -> None:
    """Validate arguments and launch stream-managed archive process."""
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    recover_and_preserve(sys.argv[1])


if __name__ == "__main__":
    main()

