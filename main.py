from stats import count_words_from_book
from stats import count_characters_from_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = count_words_from_book(book)
    num_characters = count_characters_from_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in num_characters:
        print(f"{character["name"]}: {character["count"]}")
    print("============= END ===============")
main()