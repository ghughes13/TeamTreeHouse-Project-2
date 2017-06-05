# When encoded, an "A" becomes a "Z", "B" turns into "Y", etc.
from ciphers import Cipher


class Atbash(Cipher):
    """Encrypts or Decrypts a message using Atbash"""
    global letters
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self = self

    def encrypt(self, phrase):
        """encrypts the users message with Atbash"""
        encrypted = []
        phrase = phrase.upper()
        for i in phrase:
            if i != ' ' and i in letters:
                position = -(letters.index(i) + 1)
                encrypted.append(letters[position])
            elif i == ' ':
                encrypted.append(' ')
        return "".join(encrypted)

    def decrypt(self, phrase):
        """Decrypts the users message with Atbash"""
        decrypted = []
        for i in phrase.upper():
            if i != ' ' and i in letters:
                position = -(letters.index(i) + 1)
                decrypted.append(letters[position])
            elif i == ' ':
                decrypted.append(' ')
        return "".join(decrypted)
