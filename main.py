import os


def main():
    script_dir = os.path.dirname(__file__)
    book_path = os.path.join(script_dir, "books", "frankenstein.txt")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_count_of_each_character(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    get_book_report(character_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_of_each_character(book):
    book = book.lower()
    count_of_each_character = {}

    for letter in book:
        if letter in count_of_each_character:
            count_of_each_character[letter] += 1
        else:
            count_of_each_character[letter] = 1

    return count_of_each_character


def get_book_report(character_dict):
    def sort_by_value(item):
        return item[1]

    # Filter out non-alphabetic keys
    filtered_counts = {k: v for k, v in character_dict.items() if k.isalpha()}

    sorted_dict = dict(sorted(filtered_counts.items(), key=sort_by_value, reverse=True))

    for letter, count in sorted_dict.items():
        print(f"The '{letter}' character was found {count} times.")


main()
