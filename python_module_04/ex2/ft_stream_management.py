import sys
import typing


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    if not lines:
        return ""
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed_lines) + "\n"


def read_user_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    if line.endswith("\r\n"):
        return line[:-2]
    if line.endswith("\n"):
        return line[:-1]
    return line


def save_archive_data(filename: str, content: str) -> None:
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
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.IO[str] | None = None
    content: str | None = None

    try:
        file_obj = open(filename, "r")
        content = file_obj.read()
        print("---\n")
        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)
        print("\n---")
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

    if content is None:
        return

    print("\nTransform data:")
    print("---\n")
    transformed_content: str = transform_data(content)
    if transformed_content.endswith("\n"):
        print(transformed_content, end="")
    else:
        print(transformed_content)
    print("\n---")

    new_filename: str = read_user_input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    save_archive_data(new_filename, transformed_content)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    recover_and_preserve(sys.argv[1])


if __name__ == "__main__":
    main()
