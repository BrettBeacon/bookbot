import sys
from stats import count_words, character_count, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_file_path = sys.argv[1]
    book_contents = get_book_text(book_file_path)
    count_contents = character_count(book_contents)
    sorted_list = sort_dictionary(count_contents)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()

