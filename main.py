from stats import count_words_from_book
from stats import count_characters_from_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words_from_book(book)
    print(f"{num_words} words found in the document")
    num_characters = count_characters_from_words(book)
    print(num_characters)
main()