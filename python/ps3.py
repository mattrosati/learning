# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/matteorosati/Desktop/CompSci/python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    listsecret = list(secretWord)
    if len(listsecret) == 0:
        return True
    else:
        return (listsecret[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    listsecret = list(secretWord)
    if len(listsecret) == 0:
        return ''
    else:
        if listsecret[0] in lettersGuessed:
            return listsecret[0] + " " + getGuessedWord(secretWord[1:], lettersGuessed)
        return "_ " + getGuessedWord(secretWord[1:], lettersGuessed)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remainingList = list(string.ascii_lowercase)
    for i in lettersGuessed:
        remainingList.remove(i)
    return ''.join(remainingList)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    numGuesses = 8
    lettersGuessed = []
    secretList = list(secretWord)
    while numGuesses > 0:
        print('-------------')
        print('You have ' + str(numGuesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        letterGuessed = input('Please guess a letter: ').lower()
        if letterGuessed not in lettersGuessed:
            if letterGuessed in secretList:
                lettersGuessed.append(letterGuessed)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print('-------------')
                    print('Congratulations, you won!')
                    return None
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(letterGuessed)
                numGuesses -= 1
        else:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
    print('-------------')
    print('Sorry, you ran out of guesses. The word was ' + secretWord + ".")

secretWord = chooseWord(wordlist)
hangman(secretWord)
