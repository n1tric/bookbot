def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(text)} words found in the document\n")
    char_list = get_num_letters(text)
    char_list.sort(reverse=True, key=sort_on)
    for x in char_list:
        print(f"The '{x["name"]}' character was found {x["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    char_dicts = []
    characters = {}
    for character in text.lower():
        if character.isalpha() and (character not in characters):
            characters[character] = 1
        elif character.isalpha():
            characters[character] += 1
    for key in characters:
        char_dicts.append( {"name": key, "num": characters[key]} )
    return char_dicts

main()