def mergeSortedArray(arr1: list, arr2: list) -> list:
    
    merged_array = []
    p1 =0
    
    p2 =0

    # for i in range(0, len(arr1)):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    
    while (p1 < arr1_len and p2 < arr2_len):
        if arr1[p1] <= arr2[p2]:
            merged_array.append(arr1[p1])
            p1 = p1 + 1
        else:
            merged_array.append(arr2[p2])
            p2 = p2 + 1 

    while p1 < len(arr1):
        merged_array.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        merged_array.append(arr2[p2])
        p2 += 1

    return merged_array

            
                




# b = [102,111,160,161,200]
# a = [100,115,160,165,210]



b = [1,5,10,15,16,17,18,19,20]
a = [2,5,6,7,11,14,17,111]

"""
p1 = 1, 3, 5, 7
p2 = 2, 4, 6,8

1,2, 3, 4, 5,6 , 7, 8


First create a variable to store p1
then create a variable to store p2

set the p1 and p2 at the start of arr1 and arr2 respectively

then compare element of arr1 with arr22

if value of arr1 is small then upgrade p1 to next value
else upgrade p2


"""

print(mergeSortedArray(a,b))
    
1,
"""
check every element in arr1 against every element in arr2

if element of arr1 is smaller or equal to element in arr2 append it to a list, 


[[1,3,5,7],[2,4,8,10]]

[[2,4,6,8], [1,3,5,7]]

 

"""
