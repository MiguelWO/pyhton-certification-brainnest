'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

# Path: week3\caesar_hacker.py

import caesar_cipher
import random


def caesar_brute_force(cripted):
    for key in range(1, 26):
        print(key, caesar_cipher.decrypt(cripted, key))


def main():
    print()
    print('Enter the message to cript:')
    message = input()
    print('Cripted message:')
    cripted = caesar_cipher.encrypt(message, random.randint(1, 26))
    print(cripted)

    print('Brute force attack:')
    caesar_brute_force(cripted)


if __name__ == '__main__':
    main()



