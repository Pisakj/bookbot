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

words_count = 0
letter_statistic = []

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words_count = read_words(file_contents)
    letter_statistic = list(count_letters(file_contents).items())

letter_statistic.sort(key = lambda x:x[1], reverse = True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{words_count} words found in the document")
print("")
for letter in letter_statistic:
    if letter[0].isalpha():
        print(f"The '{letter[0]}' character was found {letter[1]} times")
print("--- End report ---")