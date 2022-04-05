class StringClass:
    def __init__(self, Str):
        self.Str = Str

    def lis(self):
        return (list(self.Str))

    def length(self):
        return len(self.Str)


class PairsPossible(StringClass):
    def pairs(self, list):
        res = [(n, ob1) for idx, n in enumerate(list) for ob1 in list[idx + 1:]]
        print(res)


class SearchCommonElements(StringClass):
    def common(self, st, Str):
        a = list(set(st) & set(Str))
        print(a)


class EqualSumPairs:
    def pairs2(self, list):
        res = [sum((int(n), int(ob1))) for idx, n in enumerate(list) for ob1 in list[idx + 1:]]
        print(set(res))
        print(len(set(res)))


n = input("Enter a string :")
ob1 = StringClass(n)
print(ob1.lis())
print(ob1.length())
h = ob1.lis()
ob2 = PairsPossible(ob1)
ob2.pairs(h)
st = input("Enter string to compare ")
ob3 = SearchCommonElements(ob1)
ob3.common(n, st)
ob4 = EqualSumPairs()
ob4.pairs2(h)