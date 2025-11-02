import sys
from stats import num_words, count_characters, sort_on

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    count = num_words(text)
    
    character_dict = count_characters(text)
    sorted_characters = sort_on(character_dict)
    
    print("============ BOOKBOT ============")
    print()
    print(f"Analyzing book found at {path_to_file}...")
    print()
    print("----------- Word Count ----------")
    print()
    print(f"Found {count} total words")
    print()
    print("--------- Character Count -------")
    print()
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print()
    print("============= END ==============")


if __name__ == "__main__":
    main()

