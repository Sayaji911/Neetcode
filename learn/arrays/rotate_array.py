def rotateArray(nums: list, k: int) -> list:
    k = k % len(nums)
    print(nums[-k:])
    print(nums[k:])

    # nums[:] = nums[-k:] + nums[:-k]


print(rotateArray([1,2,3,4,5,6,7],3))

