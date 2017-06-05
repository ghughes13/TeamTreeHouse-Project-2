# This code pulls from all complete ciphers and allows you to encode messages with them.
# Should I import all classes from the beginning or have an import function that brings in the needed cipher?
# Holy Fuck; This is awesome; I've got to go back to school for computer science...

from caesar import Caesar
from atbash import Atbash
from transposition import Transposition
from keyword_cipher import Keyword

cipher_available = ["Caesar", "Atbash", "Transposition", "Keyword"]
dict_ciphers = {"caesar": Caesar, "atbash": Atbash, "transposition": Transposition, "keyword": Keyword}


def start():
    """Gets users message, cipher choice, and whether they want to encrypt or decrypt"""
    print("These are the current available ciphers: ")
    for i in cipher_available:
        print('\n' + '-' + i)
    global choice
    choice = input("\nWhich cipher would you like to use? ").lower()
    message = input("\nExcellent choice. What's the message? ")
    which_one = input("And would you like to encrypt or decrypt? ").upper()
    if which_one == "ENCRYPT":
        code_it(message, choice)
    elif which_one == "DECRYPT":
        decode_it(message, choice)
    else:
        print("That wasn't a choice. ")
        start()


def code_it(words, cipher):
    """Encrypts your message in the desired cipher. Also asks for pad and whether to display in blocks of 5"""
    global pad
    pad = input("Please enter the pad number: ")
    encoder = dict_ciphers[cipher]()
    encrypted = encoder.encrypt(words)
    string_version = encrypted
    five_space = input("Would you like your encryption in blocks of 5? y/N").upper()
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
        print("".join(this))
    else:
        print(encrypted)
    decodeyn = input("Would you like to decrypt the message as well? Y/n ")
    if decodeyn == 'n':
        again()
    else:
        decode_it(encrypted,choice)


def decode_it(words, cipher):
    """Decrypts your message in the desired cipher and confirms pad number matches."""
    pad_two = input("Please enter the pad number: ")
    if pad == pad_two:
        decoder = dict_ciphers[cipher]()
        decrypted = decoder.decrypt(words)
        print(decrypted)
        again()
    else:
        print("Error: Incorrect Pad Number. ")
        exit()


def again():
    """Runs the software again if you would like"""
    redo = input("Would you like to encrypt/decrypt something else? Y/n")
    if redo == "n":
        print("Thanks for using my encryption software!")
        exit()
    else:
        start()


name = input("What's your name? ")
print(f"\nHello {name}! This is an encryption program made so I can practice programming")
start()
