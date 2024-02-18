import typing

def maxSubArray(nums: typing.List[int]) -> int:
        '''
        
        The Intuition behind the code is to 
        find the maximum sum of a contiguous
        subarray within the given array nums.
        
        It does this by scanning through the
        array and keeping track of the current
        sum of the subarray. Whenever the 
        current sum becomes greater than the
        maximum sum encountered so far, it
        updates the maximum sum. If the current 
        sum becomes negative, it resets the 
        sum to 0 and starts a new subarray.
        By the end of the loop,
        the code returns the maximum sm.
        
        
        [-2,1,-3,4,-1,2,1,-5,4]
        
        max = -inf, -2,1, 4, 5, 6 
        cur = 0, -2, 0 , 1 , -2, 0, 4, 3, 6
        num = -2, 1 , -3, 4, -1, 2, 1 , -5 ,4 
        '''
        
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
                
            
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
       

print(maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))


def maxSubArray(self, nums: typing.List[int]) -> int:
    def kadane(i):
        if F[i] != None:
            return F[i]
        F[i] = max(nums[i],kadane(i-1) + nums[i])
        return F[i]
    n = len(nums) # store the array len
    # create a list of None of n(array len). if len = 2 then [None, None, None]
    F = [None for _ in range(n)]  
    F[0] = nums[0] # replace the first element of F to 0th element of nums.
    kadane(n-1) # pass length - 1 element into kadane function
    return max(F) # return the max element of F


nums=[-2,1,-3,4,-1,2,1,-5,4]
