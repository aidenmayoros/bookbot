import os


def main():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "books", "frankenstein.txt")

    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
        print(file_contents)


main()
