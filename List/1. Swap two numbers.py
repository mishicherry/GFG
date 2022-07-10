"""
Given a list, write a Python program to swap first and last element of the list.
Eg:
    Input : [12, 35, 9, 56, 24]
    Output : [24, 35, 9, 56, 12]
"""
#Mtd1
arr = list(map(int, input().split()))
a = arr[0]
arr[0] = arr[-1]
arr[-1] = a
print(arr) 

#Mtd2

def swapArr(ar):
    
    ar[0] , ar[-1] = ar[-1], ar[0]
    
    return ar

ar = [12, 35, 9, 56, 24]
print(swapArr(ar))
