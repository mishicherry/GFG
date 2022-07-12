"""
Count occurrences of an element in a list
Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
Output : 3 
"""

#Method1
arr = [15, 6, 7, 10, 12, 20, 10, 28, 10]
n = 10
count = 0

for i in arr:
    if i == n:
        count += 1
        
print(count)

#Method2
arr = [15, 6, 7, 10, 12, 20, 10, 28, 10]
n = 20
print(arr.count(n))

    
