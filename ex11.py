from random import randint

High = float(input("Please enter highest number: "))
Low = float(input("Please enter lowest number: "))

def RandomNumberGuess(hi,lo):

    GeneratedNumber = randint(lo,hi)
    NotCorrect = True

    while NotCorrect == True:
        guess = float(input("Guess the number: "))
        if guess == GeneratedNumber:
            print("You guessed correctly!")
            NotCorrect = False
        elif guess<GeneratedNumber:
            print("you guessed too low!")
        else:
            print("you guessed too high!")
    return

RandomNumberGuess(High,Low)


