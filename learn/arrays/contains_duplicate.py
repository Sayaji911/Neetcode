def containsDuplicate(nums: list) -> bool:
	if len(nums) > 0:
		count = {}
		for i in nums:
			if i in count:
				return True
			else:
				count[i] = 1
		
		return False

print(containsDuplicate([1,2,3,4]))







def containsDuplicate2(self, nums: List[int]) -> bool:
    if len(nums) > 0:
        count = set()
        for i in nums:
            if i in count:
                return True
            else:
                count.add(i)
        
        return False










