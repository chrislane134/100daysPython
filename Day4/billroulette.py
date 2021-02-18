# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.


import random
names_string = input(
    "Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")


total_names = len(names)

random_name = random.randint(0, total_names)

print(f"{names[random_name]} is going to buy the meal today!")
