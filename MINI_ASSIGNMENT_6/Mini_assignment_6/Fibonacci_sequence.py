#. Create a generator to return the Fibonacci sequence starting from the first element
#up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89, . . .
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b
for x in fib(12):
    print(x,end = " ")