"""
Reversing a List.
Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]
"""

#1st Mtd
lst = [10, 11, 12, 13, 14, 15]
arr = lst[::-1]
print(arr)

#2nd Mtd
lst = [10, 11, 12, 13, 14, 15]

for i in lst[::-1]:
    print(i, end=" ")
