#5.	 Merge following two Python dictionaries into one
class MERGE_TWO_DICTIONARY:
    def __init__(self,dict1,dict2):
        self.d1 = dict1
        self.d2 = dict2
        self.d3 = {}

    def merge(self):
        for item,value in self.d1.items():
            if item not in self.d3:
                self.d3[item] = value
        for item,value in self.d2.items():
            if item not in self.d3:
                self.d3[item] = value
        return self.d3


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
obj = MERGE_TWO_DICTIONARY(dict1,dict2)
print(obj.merge())