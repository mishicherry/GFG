"""
Check if element exists in list
arr= [ 1, 6, 3, 5, 3, 4 ]
x = 4
o/p: Element exists
"""

#Using for loop
arr = [ 1, 6, 3, 5, 3, 4 ]
x = int(input())

for i in range(len(arr)):
    if arr[i] == x:
        print("Element Exists!!")
        
#Using in
arr = [ 1, 6, 3, 5, 3, 4 ]
x = int(input())

if x in arr:
    print("Exists")
