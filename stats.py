

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_char():
    text = get_book_text("books/frankenstein.txt")
    lower_case = text.lower()
    text_dict = {}
    for i in range(ord('a'), ord('z')+1):
        char = chr(i)
        text_dict[char] = 0
    for char in lower_case:
        if 'a' <= char <= 'z':
            text_dict[char] += 1
    return text_dict

def sort_on(text_dict):
    return text_dict["num"]



