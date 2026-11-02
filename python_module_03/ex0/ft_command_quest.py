#!/usr/bin/env python3
import sys


def display_command_quest() -> None:
    print("=== Command Quest ===")
    
    total_args: int = len(sys.argv)
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")
    
    if total_args <= 1:
        print("No arguments provided!")
    else:
        arguments_received: int = total_args - 1
        print(f"Arguments received: {arguments_received}")
        
        index: int = 1
        user_args: list[str] = sys.argv[1:]
        for argument in user_args:
            print(f"Argument {index}: {argument}")
            index += 1
            
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    display_command_quest()