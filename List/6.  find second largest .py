"""
Program to find second largest number in a list
Input: list1 = [10, 20, 4]
Output: 10
"""

#Mtd 1
ar = [10, 20, 4]
ar.sort()
print(ar[-2]) 

new = set(ar)
print(new)

#Mtd2
ar = [10, 20, 8, 9, 18]
mx = max(ar[0], ar[1])
second_max = min(ar[0], ar[1])
n = len(ar)

for i in range(2, n):
    if ar[i] > mx:
        second_max = mx
        mx = ar[i]
    
    elif ar[i] > second_max and ar[i] != mx:
        second_max = ar[i]
        
    elif mx == second_max and second_max != ar[i]:
        second_max = ar[i]
        
print(second_max)
