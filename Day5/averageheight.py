# You are going to write a program that calculates the average student height from a List of heights.

# e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# You should not use the `sum()` or `len()` functions in your answer


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

list_total = 0
average = 0
for x in student_heights:
    list_total += x
    average += 1

print(f"this is the average {round(list_total/average, 2)}")


# solution:

# total_height = 0

# for height in student_heights:
#   total_height +=height


# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
