from typing import List


class Solution:
    @classmethod
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        sequence = 0
        current_sequnce = 1
        nums = sorted(set(nums))
        while i < len(nums):
            current_element = nums[i]
            next_element = current_element + 1
            if next_element in nums:
                current_sequnce += 1
            else:
                if current_sequnce >= sequence:
                    sequence = current_sequnce
                current_sequnce = 1
            i += 1
        return sequence

        # @classmethod
        # def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_sequence = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_sequence = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_sequence += 1

                max_sequence = max(max_sequence, current_sequence)

        return max_sequence


# nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# nums = [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]

# nums = [7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0]
nums = [0, -1]


print(Solution.longestConsecutive(nums))

"""we need to get the longest consecutive sequence
    i.e 1,2,3,4 so our output would be 4
    
    1. Sort the array [1,2,3,4,100,200]
    2. iterate from the start of the array 
        and check if the next element is 
        the increment of the current element
        a) if it is the increment of the current element
            then we will increment the sequence
        b) if not then we will break the iteration and
            start the iteration from the non sequence element
            i.e i^th el"ement and then check if the new sequence 
            is greater than the current sequence 
        

 . . .|. . . . | . .
[1,2,3,5,6,7,8,11,12]
longest_sequence = 4

"""
