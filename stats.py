def count_words(book_contents):
    split_contents = book_contents.split()
    return len(split_contents)

def character_count(book_contents):
    lower_contents = book_contents.lower()
    split_contents = lower_contents.split()

    count_characters = {}

    for word in split_contents:
        for character in word:
            if character in count_characters:
                count_characters[character] += 1
            else:
                count_characters[character] = 1
    return(count_characters)

def sort_on(items):
    return items["num"]

def sort_dictionary(char_dic):
    dict_list = []
    counter = 0

    for i, j in char_dic.items():
        dict_list.append({"char": i, "num": j})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
