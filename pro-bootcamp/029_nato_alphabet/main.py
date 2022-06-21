import pandas as pd


def get_nato_phonetic_alphabet_dict() -> dict:
    """ Returns nato phonetic alphabet using pandas
    :returns:
        (dict): A dictionary containing nato phonetic alphabet
    """
    return pd.read_csv('./nato_phonetic_alphabet.csv', index_col=0, header=None, squeeze=True, skiprows=1).to_dict()


def construct_nato_word(word:str, nato_alphabet:dict) -> list:
    """ Returns a list containing Nato Alphabet for a given word
    :param: word (str) Word to convert to Nato
    :param: nato_alphabet (dict) dictionary to use to convert to Nato
    :return: A list containing Nato words for a string
    """
    letters = [x.upper() for x in word]
    nato_letters = [nato_alphabet[letter] for letter in letters]
    print(nato_letters)


def word_validator(w:str) -> bool:
    """ Validates that word is only constructed of alpha characters.
    :param w: a string to validate
    :return:  (bool) True if it's only alphabetic characters.
    """
    return w.isalpha()


if __name__ == '__main__':
    d = get_nato_phonetic_alphabet_dict()
    is_on = True
    while is_on:
        word = input("Enter a word for converting to nato alphabet:")
        if word_validator(word):
            construct_nato_word(word, d)
            n = input("Continue? y/n: ")
            if n == "n":
                is_on = False
        else:
            print("Invalid word, use characters only and no spaces.")
