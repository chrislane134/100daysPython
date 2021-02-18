# You are going to write a program which will mark a spot with an X.
# First your program must take the user input and convert it to a usable format.

# Next, you need to use it to update your nested list with an "x".

# # Example Input 1

# column 2, row 3 would be entered as:

# ```
# 23
# ```

# # Example Output 1

# ```
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']
# ```


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column_number = int(position[0]) - 1
row_number = int(position[1]) - 1

map[row_number][column_number] = "x"


print(f"{row1}\n{row2}\n{row3}")
