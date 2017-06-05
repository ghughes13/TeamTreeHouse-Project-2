# The Affine cipher is a monoalphabetic substitution cipher and it can be the exact same as a standard Caesarian shift
# when "a" is 1. Mathematically, it is represented as e(x) = (ax + b) mod m. Decryption is a slightly different
# formula, d(x) = a-1(x - b) mod m.

from ciphers import Cipher

class Affine(Cipher):

    def __init__(self):
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass
