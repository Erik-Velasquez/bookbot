from stats import get_num_words, get_num_chars, order
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    ordered = order(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(ordered)):
        if ordered[i]["char"].isalpha():
            print(f"{ordered[i]["char"]}: {ordered[i]["num"]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
