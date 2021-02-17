# Write a program that works out whether if a given number is an odd or even number.


number = int(input("Which number do you want to check? "))

check_number = number % 2

if check_number == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
