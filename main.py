def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = get_book_contents(path_to_book)
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)
    print_report(word_count, character_count)


def get_book_contents(path):
    with open(path) as f:
        contents = f.read()
        return contents


def get_word_count(book_contents):
    return len(book_contents.split())


def get_character_count(book_contents):
    output = {}
    words = book_contents.split()
    for word in words:
        for char in word:
            if char.lower() in output:
                output[char.lower()] += 1
            else:
                output[char.lower()] = 1
    return output


def sort_on(dict):
    return dict[list(dict.keys())[0]]


def print_report(word_count, character_count):
    sorted_character_count = []
    for char in character_count:
        if char.isalpha():
            sorted_character_count.append({char: character_count[char]})
    sorted_character_count.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for char_dict in sorted_character_count:
        key = list(char_dict.keys())[0]
        value = char_dict[key]
        print(f"The \'{key}\' character was found {value} times")
    print("--- End report ---")
main()