from typing import List


class Solution:
    pass


class ContainsDuplicates(Solution):
    def using_hash_set(self, nums: List[int]) -> bool:
        """Using HashSet with Time Complexity O(n) and Space Complexity O(1)"""
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

    def using_brute_force(self, nums: List[int]) -> bool:
        """Brute force approach with Time Complexity O(n^2) and Space Complexity O(1)"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    def using_sort_and_match(self, nums: List[int]) -> bool:
        """Sort and Match adjacent approach with Time Complexity O(n log n) and Space Complexity O(1)"""
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


n_nums = [
    [1, 2, 3, 4],
    [1, 2, 3, 1],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]

contains_duplicates = ContainsDuplicates()

for nums in n_nums:
    print(f"Input: {nums}")
    print("Using HashSet:", contains_duplicates.using_hash_set(nums))
    print("Using Brute Force:", contains_duplicates.using_brute_force(nums))
    print("Using Sort and Match:", contains_duplicates.using_sort_and_match(nums))
    print()
