def sort_on(items):
    return items["count"]

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def get_word_count(file_path):
    contents = get_book_text(file_path)
    words = contents.split()
    return len(words)

def get_character_count(file_path):
    content = get_book_text(file_path)
    content = content.lower()
    chars = {}
    for char in content:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_sorted_chars(chars_dict):
    sorted_chars = []
    for key in chars_dict:
        if key.isalpha():
            sorted_chars.append({"char": key, "count": chars_dict[key]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars