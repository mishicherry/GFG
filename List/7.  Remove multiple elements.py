"""
Remove multiple elements from a list
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], 
        New_List = [15, 10]
"""

#Mtd 1
orig = [12, 15, 3, 10]
rem = [12, 3]

new = set(orig) - set(rem)
new_list = list(new)
print(new_list)


#Mtd2
orig = [12, 15, 3, 10]
rem = [12, 3]

orig = [ele for ele in orig if ele not in rem]
print(orig)

