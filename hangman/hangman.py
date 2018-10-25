# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    SplitWord = str.split(secret_word)
    for e in SplitWord:
        if e not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_Word = []
    SplitWord = str.split(secret_word)
    for e in SplitWord:
        if e in letters_guessed:
            guessed_Word.append(e)
        else:
            guessed_Word.append("_")
    return str(guessed_Word)

def get_available_letters(letters_guessed):

    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    NotUsedLetters = []
    for e in Alphabet:
        if e not in letters_guessed:
            NotUsedLetters.append(e)

    return str(NotUsedLetters)

def hangman(secret_Word):
    guess_Count = 6
    guess_letter = []
    bary = False
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("The secret word contains ", len(secret_Word), " letters")
    while bary == False:
        print("You have ", guess_Count, " guesses")
        guess_letter.append(input("Please enter your guess: "))
        if is_word_guessed(secret_Word,guess_letter):
            print("You win, you guessed the word!")
            bary == True
        print("The Avaliable letters are:", get_available_letters(guess_letter))
        print(get_guessed_word(secret_Word,guess_letter))


wordlist = load_words()
secret_word = choose_word(wordlist)
hangman(secret_word)
