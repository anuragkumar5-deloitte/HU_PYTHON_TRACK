#6.	 Rename key city to location in the following dictionary
class RENAME_DICTIONARY:
    def __init__(self):
        self.d = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
        self.new_key = "location"

    def modify(self):
        x = self.d.pop("city")
        self.d[self.new_key] = x
        return self.d


obj = RENAME_DICTIONARY()
print(obj.modify())