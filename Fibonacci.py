Fib_Value = int(input("Please enter the nth fibonacci: "))
Answer = 0
Second_Last_Number = 0
Last_Number = 1


def fib(fib_value, second_last_number, last_number, answer):

    answer = Last_Number + second_last_number

    second_last_number = Last_Number
    last_number = Answer

    if fib_value == 0:
        return answer
    else:
        fib(fib_value-1, second_last_number, last_number, answer)


print(fib(Fib_Value, Second_Last_Number, Last_Number, Answer))