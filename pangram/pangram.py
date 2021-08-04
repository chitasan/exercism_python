import string

def is_pangram(sentence):
    if set(sentence.lower()) >= set(string.ascii_lowercase):
        return True
    else:
        return False
