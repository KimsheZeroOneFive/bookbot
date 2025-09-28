from stats import (get_book_text, 
                   get_num_words, 
                   get_characters, 
                   get_char_sorted
                   )
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = get_book_text(filepath)
    words = get_num_words(text)
    chars = get_characters(text)
    sorted_chars = get_char_sorted(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()