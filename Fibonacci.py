Fib_Value = int(input("Please enter the nth fibonacci: "))
Second_Last_Number = 0
Last_Number = 0


def fib(fib_value, second_last_number, last_number):

    answer = last_number + second_last_number

    if fib_value == 2:
        return answer
    else:
        second_last_number = last_number
        last_number = answer
        if last_number == 0:
            last_number = 1
        return fib(fib_value-1, second_last_number, last_number)


print(fib(Fib_Value, Second_Last_Number, Last_Number))
