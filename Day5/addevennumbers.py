# You are going to write a program that calculates the sum of all the even numbers from 1 to 100


total = 0

for number in range(2, 101, 2):
    total += number

print(total)
