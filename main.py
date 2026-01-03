import sys
from stats import counter, ch_count, sort


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    the_string = get_book_text(filepath)
    count = counter(the_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    character_count = ch_count(filepath)
    sorted = sort(character_count)
    for f in sorted:
        ch = f["char"]
        if ch.isalpha() == True:
            print(f"{ch}: {f["num"]}")

    print("============= END ===============")

main()

