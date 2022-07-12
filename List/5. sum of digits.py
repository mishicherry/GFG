"""
Sum of number digits in List
arr = [12, 67, 98, 34]
o/p:  [3, 13, 17, 7]

"""

#
arr = [12, 67, 98, 34]
new = []

for i in arr:
    sum = 0
    for j in str(i):
        sum += int(j)
    new.append(sum)
    
print(new)
        
