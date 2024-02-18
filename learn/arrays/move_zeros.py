"""
[0,1,0,3,12]
[0,1,0,3,12]
[0,0,1,3,12]


n = len = 5
i = 0
temp = 1

if num[i] != 0:
    temp = num[i+1]
    num[i+1] = num[i]
    num[i] = temp
    





"""



import typing


def moveZeroes(nums: typing.List[int]) ->  typing.List[int]:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]
        
        if nums[j] != 0:
            j += 1
    
    print(nums)
    
    
            
moveZeroes(nums=[0,1,0,3,12])



def moveZerosTwo(nums: typing.List[int]) -> list:
    snowball : int = 0 # number of zeroes encountered
    for i in range(len(nums)):
        if nums[i] == 0:
            snowball += 1
        else:
            if snowball > 0:
                temp = nums[i]
                nums[i] = nums[i - snowball]
                nums[i - snowball] = temp
                
nums=[1,3,12,0,0]
snowball = 0, 1, 2, 
i = 0, 1, 2, 3, 4
temp = 1, 3, 12
nums[i] = 0, 0, 0
