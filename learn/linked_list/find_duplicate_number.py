from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        
        We are using Floyds Cycle Detection Algorithm
        https://cp-algorithms.com/others/tortoise_and_hare.html#problems
        
        '''
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

k    = [0, 1, 2 ,3, 4]
nums = [1, 3, 4, 2, 2]
sol = Solution()

sol.findDuplicate(nums=[1, 3, 4, 2, 2])
print(sol)
