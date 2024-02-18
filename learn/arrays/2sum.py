'''
eg: nums = [2,7,11,15], t = 9 , [0,1]
brute force :

take every element and iterate over the nums
and add it with every other element until it equals the target

2 - 7,11,15
7 - 2,11,15
11 - 2,7, 15
15 - 2,7,11

'''

def twoSums(nums: list, target: int) -> list:
    '''
    create a dict seen 
    
    in this
    
    store the key as the difference bw target and element of num
    
    and value as the index of the element of num
    '''
    
    seen = {}
    
    for i,j in enumerate(nums):
        remaining = target - nums[i]
                     
        if remaining in seen:
            return [i, seen[remaining]]
        else:
            seen[j] = i

nums = [2,11,15,7]
target = 9


remaining = 7,2,
seen = {2:0,}

print(twoSums(nums,target))