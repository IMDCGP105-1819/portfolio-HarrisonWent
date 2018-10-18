from random import randint

High = float(input("Please enter highest number: "))
Low = float(input("Please enter lowest number: "))

def RandomNumberGuess(hi, lo):
    GeneratedNumber = randint(lo,hi)
    Guess = float(input("Guess the number: "))
    if Guess == GeneratedNumber:
        print("You guessed correctly!")
    return

RandomNumberGuess(High,Low)


