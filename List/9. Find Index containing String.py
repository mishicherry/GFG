"""
Find Index containing String in List
i/p: [2, 'a', 'b', 7, 9, 'c']
o/p: 1, 2, 5
"""

list1 = [2, 'a', 'b', 7, 9, 'c'] 

for i in range(0, len(list1)):
    if type(list1[i]) == str:
        print(i, end=" ")
        
