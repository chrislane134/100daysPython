for number in range(1, 101):

    if not number % 3 and not number % 5:
        print("FizzBuzz")
    elif not number % 3:
        print("fizz")
    elif not number % 5:
        print("buzz")
    else:
        print(number)


# Solution given:

# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 ==0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("fizz")
#   elif number % 5 == 0:
#     print("buzz")
#   else:
#     print(number)
