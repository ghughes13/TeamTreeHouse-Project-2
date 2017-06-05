# Simple Transposition Cipher
# the sky is blue : eulb si yks eht

from ciphers import Cipher


class Transposition(Cipher):

    def __init__(self):
        self = self

    def encrypt(self, phrase):
        """Encrypts users message with Transposition Cipher"""
        encrypted = []
        seperate = phrase.split(" ")
        for word in seperate:
            encrypted.append(word[::-1])
        final_encrypted_message = " ".join(encrypted[::-1]).upper()
        return final_encrypted_message

    def decrypt(self, phrase):
        """Decrypts users message with Transposition Cipher"""
        decrypted = []
        seperate = phrase.split(" ")
        for word in seperate:
            decrypted.append(word[::-1])
        final_decrypted_message = " ".join(decrypted[::-1]).upper()
        return final_decrypted_message
