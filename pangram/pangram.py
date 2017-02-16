from string import ascii_lowercase
def is_pangram(sentence):
    return len(set([letter for letter in sentence.lower() if letter in ascii_lowercase])) == 26
