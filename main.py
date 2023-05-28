def read_words(text):
    return len(text.split())

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(read_words(file_contents))
