High = float(input("Please enter highest number: "))
Low = float(input("Please enter lowest number: "))
for Number in range (1,100):
    if Number % 3 == 0 & Number % 5:
        print("FizzBuzz")
    elif Number % 5 == 0:
        print("Buzz")
    elif Number % 3 == 0:
        print("Fizz")
    else:
        print(Number)