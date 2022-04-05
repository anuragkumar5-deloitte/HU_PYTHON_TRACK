#4.	Map the dictionary in the following manner
#Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]

class MAP_DICTIONARY:
    def __init__(self,list1,list2):
        self.l1 = list1
        self.l2 = list2
        self.d = {}

    def mergeDict(self):
        if len(self.l1) == len(self.l2):
            for x in range(len(self.l1)):
                self.d[self.l1[x]] = self.l2[x]
            return self.d
        else:
            print("Invalid input..!!")
        return self.d


list1 = ['Ten','Twenty','Thirty']
list2 = [10,20,30]
obj = MAP_DICTIONARY(list1,list2)
print(obj.mergeDict())