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
    sorted_count = []
    for character in count:
        if character.isalpha():
            sorted_count.append( { "name": character, "count": count[character]})
    sorted_count.sort(key = sort_characters, reverse=True)
    return sorted_count
    
def sort_characters(character_count):
    return character_count["count"]

