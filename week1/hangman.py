'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''


def hangman(word, tries, used_letters=None, guess_word=None):
    if used_letters is None and guess_word is None:
        used_letters = []
        guess_word = ["_" for i in word]
    guess = input("Enter the letter to guess")

    while guess in used_letters and guess.isnumeric():
        if guess.isnumeric():
            guess = input("Is a number, Enter the letter to guess")
        elif guess in used_letters:
            guess = input("You have already chose that letter, Enter the letter to guess")

    string = f'You have {tries} tries left.' + '\n'
    lst = ' '.join(used_letters)
    string += f'Used letters: {lst}' + '\n'
    # guess_word = "_" * len(word)
    lst = " ".join(guess_word)
    string += lst + '\n'
    string += f'Guess a letter: {guess}' + '\n'
    print(string)
    if tries < 0:
        print(f'You lose')
        return False
    if guess in word:
        used_letters.append(guess)
        for i in range(len(guess_word)):
            if word[i] == guess:
                guess_word[i] = guess
        # index = word.index(guess)
        # guess_word[index] = word[index]
        lst = "".join(guess_word)
        if lst == word:
            print(f'You guesses the word {word} !')
            return True
        hangman(word, tries, used_letters, guess_word)
    else:
        tries -= 1
        used_letters.append(guess)
        hangman(word, tries, used_letters, guess_word)


if __name__ == "__main__":
    hangman("java", 6)

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
