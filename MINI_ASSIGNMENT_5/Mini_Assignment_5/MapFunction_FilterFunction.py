#Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.
#Note: map() function is inside filter() function.
#lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
from functools import reduce
def problem3():
    list1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
    new_list = filter(lambda y: (y < 0), list1)
    print("list update______")
    for x in new_list:
        print(abs(x), end=' ')
    print()



#Take the first two values, run the function on them.
# Then take the result and the next value and have a multiplication between them. etc.
# When no more values are left, return the last result.
#Note: use reduce function for this




#Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
#lst1=["Netflix", "Hulu", "Sling", "Hbo"]
#lst2=[198, 166, 237, 125]
def problem5():
    list1 = ["Netflix", "Hulu", "Sling", "Hbo"]
    list2 = [198, 166, 237, 125]
    if len(list1) == len(list2):
        new_dict = {list1[i]: list2[i] for i in range(len(list1))}
        print("\nCreated dictionary______", new_dict)
    else:
        print("Invalid Input_____")
problem3()
problem5()
