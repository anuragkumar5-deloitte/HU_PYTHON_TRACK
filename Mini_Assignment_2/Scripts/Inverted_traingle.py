row = int(input('Enter number of rows required: '))

# Loop through rows
for i in range(1, row + 1):

    # Loop through columns
    for j in range(1, row + 1):

        # Printing Pattern
        if (j == row) or (i == 1) or (i == j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()