def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def count_words_from_book(book):
    count = 0
    words = book.split()
    for word in words:
        count += 1
    return count

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words_from_book(book)
    print(f"{num_words} words found in the document")

main()