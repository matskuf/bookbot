from stats import counter, ch_count, sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "books/frankenstein.txt"
    the_string = get_book_text(filepath)
    count = counter(the_string)
    print(f"Found {count} total words")
    character_count = ch_count(filepath)
    print(character_count)
    sorted = sort(character_count)
    print(sorted)

main()

