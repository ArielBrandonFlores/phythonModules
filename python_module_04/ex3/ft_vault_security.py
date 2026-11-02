def secure_archive(
    filename: str,
    action: str | int = "read",
    content: str | None = None,
) -> tuple[bool, str]:
    """Provide safe access to a file using context manager (with)."""
    try:
        if action in ("read", 0):
            with open(filename, "r") as archive_file:
                return (True, archive_file.read())
        elif action in ("write", 1):
            with open(filename, "w") as archive_file:
                if content is not None:
                    archive_file.write(content)
                return (True, "Content successfully written to file")
        return (False, f"Invalid action: {action}")
    except OSError as error:
        return (False, str(error))


def main() -> None:
    """Demonstrate secure vault operations complying with subject examples."""
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    inaccessible_file: str = "/etc/master.passwd"
    read_perm_result: tuple[bool, str] = secure_archive(inaccessible_file)
    if "No such file" in read_perm_result[1]:
        inaccessible_file = "/etc/shadow"
        read_perm_result = secure_archive(inaccessible_file)
    print(read_perm_result)

    sample_content: str = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    temp_source: str = "/tmp/sample_ancient_fragment.txt"
    with open(temp_source, "w") as source_fp:
        source_fp.write(sample_content)

    print("\nUsing 'secure_archive' to read from a regular file:")
    read_success: bool
    retrieved_data: str
    read_success, retrieved_data = secure_archive(temp_source)
    print((read_success, retrieved_data))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    temp_dest: str = "/tmp/sample_vault_copy.txt"
    write_result: tuple[bool, str] = secure_archive(
        temp_dest, "write", retrieved_data
    )
    print(write_result)


if __name__ == "__main__":
    main()
