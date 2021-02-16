# Data Types

# Instructions

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# **Warning.** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# two_digit_number = input("Type a two digit number: ")   (original effort)
# value1 = int(two_digit_number[0])
# value2 = int(two_digit_number[1])
# total = value1 + value2
# print(total)


two_digit_number = input("Type a two digit number: ")
total = int(two_digit_number[0]) + int(two_digit_number[1])
print(total)
