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


def vernam_cipher(text, key):
    len_of_text = len(text)
    len_of_key = len(key)

    if len_of_text > len_of_key:
        desired_length = len_of_text - len_of_key
        padded_key = (key * ((desired_length // len(key)) + 1))[:desired_length]
        new_key = key + padded_key
        cipher_keys_list = get_keys_for_alphabets(new_key)

    else:
        cipher_keys_list = get_keys_for_alphabets(key)

    plain_list = get_keys_for_alphabets(text)
    cipher_text_list = [(p + k) % 26 for (p, k) in zip(plain_list, cipher_keys_list)]
    cipher_chars = [key_table()[val] for val in cipher_text_list]
    cipher_text = "".join(cipher_chars)
    return cipher_text


if __name__ == "__main__":
    print(vernam_cipher("gotohell", "harama"))
