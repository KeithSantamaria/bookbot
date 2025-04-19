def count_words_from_book(book):
    count = 0
    words = book.split()
    for word in words:
        count += 1
    return count

def count_characters_from_words(book):
    count = {}
    words = book.split()
    for word in words:
        characters = list(word)
        for character in characters:
            converted_character =character.lower()
            if converted_character in count:
                count[converted_character] += 1
            else:
                count[converted_character] = 1
    return count

