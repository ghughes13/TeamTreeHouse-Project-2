# The Keyword cipher is identical to the Caesar Cipher with the exception that the substitution alphabet
# used can be represented with a keyword.

# To create a substitution alphabet from a keyword, you first write down the alphabet. Below this you write
# down the keyword (omitting duplicate letters) followed by the remaining unused letters of the alphabet.

# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# KEYWORDABCFGHIJLMNPQSTUVXZ

# To encipher a plaintext message, you convert all letters from the top row to their correspondng letter
# on the bottom row (A to K, B to E, etc).

#I plan to move lines 25-34 into a seperate function and just call that at the begining of encrypt and decrypt (DRY)

from ciphers import Cipher


class Keyword(Cipher):

    def __init__(self):
        self = self

    def encrypt(self, phrase):
        """Encrypts the users message as a Keyword Cipher"""
        keyword = input("What keyword would you like to use? ")
        plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = []
        encrypted = []
        for i in keyword.upper():
            if i not in ciphertext:
                ciphertext.append(i)
        for i in plaintext:
            if i not in ciphertext:
                ciphertext.append(i)

        key_dict = dict(zip(plaintext, ciphertext))

        for i in phrase.upper():
            if i == " ":
                encrypted.append(" ")
            else:
                for key, value in key_dict.items():
                    if i == key:
                        encrypted.append(value)

        return "".join(encrypted)

    def decrypt(self, phrase):
        """Decrypts the users message with a Keyword Cipher"""
        keyword = input("What keyword is it encrypted with? ")
        plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = []
        decrypted = []
        for i in keyword.upper():
            if i not in ciphertext:
                ciphertext.append(i)
        for i in plaintext:
            if i not in ciphertext:
                ciphertext.append(i)

        key_dict = dict(zip(plaintext, ciphertext))

        for i in phrase.upper():
            if i == " ":
                decrypted.append(" ")
            else:
                for key, value in key_dict.items():
                    if i == value:
                        decrypted.append(key)

        return "".join(decrypted)