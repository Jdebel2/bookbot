import sys
from stats import get_word_count, get_character_count, get_sorted_chars


def report(relative_file_path):
    word_count = get_word_count(relative_file_path)
    char_count = get_sorted_chars(get_character_count(relative_file_path))
    print("============ BOOKBOT ============\nAnalyzing book found at " + str(relative_file_path) + "...\n----------- Word Count ----------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count -------")
    for c in char_count:
        print(str(c['char']) + ": " + str(c['count']))
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    report(path_to_book)

main()