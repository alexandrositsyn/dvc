import os
import sys


DIR_PATH = "data"

def main():
    for file in os.listdir(DIR_PATH):
        file_name = os.fsdecode(file)
        if file_name.endswith(".txt"):
            print(f"Reading {file_name}")
            with open(os.path.join(DIR_PATH, file_name), "r") as file_pointer:
                file_contents = file_pointer.readlines()
                result = f"File contents:\n{''.join(file_contents)}\n"
                sys.stdout.write(result)


if __name__ == "__main__":
    main()
