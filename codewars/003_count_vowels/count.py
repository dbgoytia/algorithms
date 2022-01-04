def get_count(sentence):
    return sum(1 for letter in sentence if letter in "aeiou")