#1.	Return all the duplicate values from list of arraylist
class DUPLICATELIST:
    def __init__(self):
        self.x = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

    def DUPLICATE(self):
        dict = {}
        for item in self.x:
            for y in item:
                if y not in dict:
                    dict[y] = 1
                else:
                    dict[y] += 1
        for key,value in dict.items():
            if value > 1:
                print(key, " --> ", value)


obj = DUPLICATELIST()
obj.DUPLICATE()