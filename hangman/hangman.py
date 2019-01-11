# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"

#loads words into list
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

#choses random word from list
def choose_word(wordlist):
    return random.choice(wordlist)

#checks if word has been guessed
def is_word_guessed(secret_word, letters_guessed):
    SplitWord = str.split(secret_word)
    for e in SplitWord:
        if e not in letters_guessed:
            return False
    return True

#displays current correctly guessed letters
def get_guessed_word(secret_word, letters_guessed):
    guessed_Word = []
    SplitWord = list(secret_word)
    correct_count = 0
    letters_guessed = list(dict.fromkeys(letters_guessed))
    for e in SplitWord:
        found = False
        for guessed_letter in letters_guessed:
            if e == guessed_letter:
                guessed_Word.append(e)
                found = True
        if not found:
            guessed_Word.append("_")
        else:
            correct_count+=1
    return str(guessed_Word)

#displays remaining letters than haven't been used to guess
def get_available_letters(letters_guessed):

    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    NotUsedLetters = []
    for e in Alphabet:
        if e not in letters_guessed:
            NotUsedLetters.append(e)

    return str(NotUsedLetters)

#gameplay loop
def hangman(secret_Word):
    guess_Count = 6
    guess_letter = []
    Guessed = False

    print("The secret word contains ", len(secret_Word), " letters")

    while not Guessed:
        print("The Avaliable letters are:", get_available_letters(guess_letter))
        print(get_guessed_word(secret_Word,guess_letter))

        print("You have ", guess_Count, " guesses")
        guess_letter.append(input("Please enter your guess: "))

        if is_word_guessed(secret_Word,guess_letter):
            print("You win, you guessed the word!")
            Guessed = True

        if guess_letter[-1] in secret_word:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly!")
            guess_Count-=1
            if guess_Count == 0:
                print("Out of goes! The answer is:", secret_word)
                Guessed = True


wordlist = load_words()
secret_word = choose_word(wordlist)
hangman(secret_word)
