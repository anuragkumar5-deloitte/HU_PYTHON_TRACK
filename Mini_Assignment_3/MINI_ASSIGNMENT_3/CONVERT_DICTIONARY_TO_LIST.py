#7.	Convert Dictionary to list
class CONVERT_DICTIONARY_TO_LIST:
    def __init__(self,d):
        self.l = []
        self.d = d

    def convert(self):
        for key,value in self.d.items():
            flag = []
            flag.append(key)
            for item in value:
                flag.append(item)
            self.l.append(flag)
        return self.l


d = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
obj = CONVERT_DICTIONARY_TO_LIST(d)
print(obj.convert())