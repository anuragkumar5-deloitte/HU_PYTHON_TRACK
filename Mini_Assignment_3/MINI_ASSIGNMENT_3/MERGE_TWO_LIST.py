#2.	Merge two lists as shown below
class MARGE_TWO_LIST:
    def __init__(self, list1, list2):
        self.l1 = list1
        self.l2 = list2
        self.l3 = []

    def mergeData(self):
        for x in self.l1:
            for y in self.l2:
                new_data = x + y
                self.l3.append(new_data)
        return self.l3


list1 = ["HELLO", "TAKE"]
list2 = ["DEAR", "SIR"]
obj = MARGE_TWO_LIST(list1, list2)
print(obj.mergeData())
