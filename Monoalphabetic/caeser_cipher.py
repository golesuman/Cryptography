import string


def alphabet_table():
    alphabets_ = {}
    alphabets = string.ascii_lowercase
    for i, alphabet in zip(range(26), alphabets):
        alphabets_[alphabet] = i

    return alphabets_


def key_table():
    keys = {}
    alphabets = string.ascii_lowercase

    for i, alphabet in zip(range(26), alphabets):
        keys[i] = alphabet

    return keys


def get_keys_for_alphabets(text):
    return [alphabet_table()[char] for char in text]


def caeser_cipher(text, key):
    plain_list = get_keys_for_alphabets(text)
    cipher_list = [(x + key) % 26 for x in plain_list]
    cipher_chars = [key_table()[val] for val in cipher_list]
    cipher_text = "".join(cipher_chars)
    print(cipher_text)
    return cipher_text


if __name__ == "__main__":
    caeser_cipher("sumangole", 5)
