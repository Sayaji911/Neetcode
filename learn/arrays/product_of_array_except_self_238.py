def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize left and right product arrays
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate left products
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product
    
    # Calculate right products
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product
    
    # Calculate the final result
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

# Example usage:
nums = [1, 2, 3, 4]
# result = productExceptSelf(nums)
# print(result)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    left = []
    product = 1
    for i in nums:
        product *= i
        left.append(product)
    
    right = []
    product = 1
    
    for i in range(len(nums)-1,-1,-1,):
        product *= nums[i]
        right.append(product)
        
    result = [left[i] * right[i] for i in range(len(nums))]

    return result

def productExceptSelf1(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
        
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


# nums = [1, 2, 3, 4]
# result = productExceptSelf1(nums)
# print(result)


def productExceptSelf1(nums: List[int]) -> List[int]:
    left = []
    product = 1
    
    for i in nums:
        product *= i
        left.append(product)
    
    right = [1] * len(nums)
    product = 1
    
    for i in range(len(nums) -1 , -1,-1):
        product *= nums[i]
        right[i] = product    

    op = [1] * len(nums)
    
    op[0] = right[1]

    for i in range(1,len(nums) - 1):
        t = left[i-1] * right[i+1]
        op[i] = t

    op[len(nums) - 1] = left[len(nums) - 2]
    
    
    
    return op
    
# nums = [1, 2, 3, 4]
# result = productExceptSelf1(nums)
# print(result)


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = [1] * n
        right = [1] * n

        product_left = 1
        for i in range(n):
            left[i] = product_left
            product_left *= nums[i]
            
        product_right = 1
        for i in range(n - 1, -1, -1):
            right[i] = product_right
            product_right *= nums[i]

        output = [left[i] * right[i] for i in range(n)]
        
        return output
    
    
        
# nums = [1, 2, 3, 4]
# result = Solution.productExceptSelf(nums)
# print(result)



def test(nums: List):
    res = [1] * len(nums)
    
    prefix = 1
    
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    print(res)
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):    
        print(i)
        res[i] *= postfix
        postfix *= nums[i] 
    
    print(res)
    

nums = [1, 2, 3, 4]
result = test(nums)
print(result)