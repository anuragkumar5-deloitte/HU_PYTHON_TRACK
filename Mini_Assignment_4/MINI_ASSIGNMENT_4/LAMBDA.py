def solution1():
    ans = lambda a, x, b, c: ((a * (x * x)) + (b * x) + c)
    print(ans(1, 2, 3, 4))


def solution2():
    val = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
    count_of_a = list(map(lambda x:x.count("a"),val))
    count_of_A = list(map(lambda x:x.count("A"),val))
    print(count_of_a)
    print(count_of_A)
solution1()
solution2()