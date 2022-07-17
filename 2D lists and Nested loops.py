"""in 2D lists is just a normal type of list but the items of the list are lists themselves,
they are  arrranged in columns and row like,
and that is how they are accessed,by inputing their row and column index respectively"""

numbers= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numbers[3][0])
print(numbers[0][1])

#a nested for loop is a for loop inside of a for loop

for rows in numbers:
    for col in rows:
        print(col)

