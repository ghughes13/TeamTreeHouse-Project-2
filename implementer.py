from ciphers import Cipher
from atbash import Atbash
from caesar import Caesar
from transposition import Transposition
from keyword_cipher import Keyword


class Implement(Cipher):

    dict_ciphers = {"caesar": Caesar, "atbash": Atbash, "transposition": Transposition, "keyword": Keyword}

    def __init__(self):
        self = self

    def encrypt(self, words, cipher):
        """Encrypts the users message with the desired cipher. Also requires a pad"""
        no_white = []
        global pad
        pad = input("Please enter the pad number: ")
        encoder = self.dict_ciphers[cipher]()
        encrypted = encoder.encrypt(words)
        string_version = encrypted
        five_space = input("Would you like your encryption in blocks of 5? Warning: This will interfere with correct "
                           "decryption spacing. y/N").upper()
        if five_space == 'Y':
            no_white = []
            this = []
            for i in string_version:
                if i != " ":
                    no_white.append(i)
            count = 0
            for i in no_white:
                this.append(i)
                count += 1
                if count == 5:
                    count = 0
                    this.append(" ")

            return "".join(this)
        else:
            return encrypted

    def decrypt(self, words, cipher):
        """Decrypts the users message with the desired cipher. Also requires pad, but if entered incorrectly exits"""
        pad_two = input("Please enter the pad numebr: ")
        if pad == pad_two:
            decoder = self.dict_ciphers[cipher]()
            decrypted = decoder.decrypt(words)
            return decrypted
        else:
            print("Error: Incorrect Pad Number. ")
            exit()


