##a. Write a program to input an integer N from user and print pascal triangle up to N rows.
class PascalTriangle:
    def __init__(self):
        self.n = 0
    def getNumber(self, x, y):
        num = 1
        if y > x - y:
            y = x - y
        for i in range(0, y):
            num = num * (x - i)
            num = num // (i + 1)
        return num

    def printTriangle(self):
        rows = int(input("Enter no. of lines..."))
        # i  represents row
        for i in range(0, rows):
            # j represents column
            for j in range(0, i + 1):
                print(self.getNumber( i, j), end=" ")
            print()


obj = PascalTriangle()
obj.printTriangle()