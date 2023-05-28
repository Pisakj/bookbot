def read_words(text):
    return len(text.split())

def count_letters(text):
    fin_dict = {}
    for ch in text:
        if ch.lower() in fin_dict:
            fin_dict[ch.lower()] += 1
        else:
            fin_dict[ch.lower()] = 1
    return fin_dict

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(read_words(file_contents))
    print(count_letters(file_contents))
