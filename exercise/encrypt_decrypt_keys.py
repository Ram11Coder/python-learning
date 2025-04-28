import random
import string

chars = " " + string.digits + string.ascii_letters + string.punctuation
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)


# ENCRYPT
def encrypt():
    plain_text = input("Enter the message to encrypt : ")
    encrypt_text = ""
    for text in plain_text:
        index = chars.index(text)
        encrypt_text += keys[index]
    print(f"encrypted message : {encrypt_text}")


# ENCRYPT
def decrypt():
    encrypt_text = input("Enter the message to decrypt : ")
    original = ""
    for text in encrypt_text:
        index = keys.index(text)
        original += chars[index]

    print(f"original message : {original}")


if __name__ == '__main__':
    encrypt()
    decrypt()
