'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, key):
    encrypted = ''
    for char in message.upper():
        if char in LETTERS:
            index = LETTERS.find(char)
            index = (index + key) % 26
            encrypted += LETTERS[index]
        else:
            encrypted += char
    return encrypted


def decrypt(message, key):
    decrypted = ''
    for char in message.upper():
        if char in LETTERS:
            index = LETTERS.find(char)
            index = (index - key) % 26
            decrypted += LETTERS[index]
        else:
            decrypted += char
    return decrypted


def main():
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    choice = input('> ').lower()
    if choice == 'e':
        print('Please enter the key (0 to 25) to use.')
        key = int(input('> '))
        print('Enter the message to encrypt.')
        message = input('> ')
        print(encrypt(message, key))
    elif choice == 'd':
        print('Please enter the key (0 to 26) to use.')
        key = int(input('> '))
        print('Enter the message to decrypt.')
        message = input('> ')
        print(decrypt(message, key))
    else:
        print('Please enter e or d.')

if __name__ == '__main__':
    main()

