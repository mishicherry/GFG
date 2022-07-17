"""
Get the indices of all occurrences of an element in a list
Input: [1, 2, 3, 1, 5, 4]
O/p: 0, 3
"""

#Method 1
l1 = [1, 2, 3, 1, 5, 4]

for i in range(0, len(l1)):
    if l1.count(l1[i]) > 1:
        print(i, end=" ")
        

