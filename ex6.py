my_name = input("What is your name? ")
my_age = int(input("How old are you? "))
my_height = int(input("How tall are you? "))
my_weight = int(input("How much do you weigh? "))
my_eyes = input("What colour eyes do you have? ")
my_hair = input("What colour hair do you have? ")
is_heavy = my_weight > 3000

print(f"Let's talk about {my_name}.")

print(f"He is {my_height} inches tall.")
if my_height > 200:
    print("That's really tall!")

print(f"He's {my_weight} pounds heavy.")
if is_heavy>0:
    print(f"It is {is_heavy} that he is overweight.")

print(f"He's got {my_eyes} eyes and {my_hair} hair.")

if my_age>100:
    print("You are over 100! that's really old!")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}")