from typing import List
from collections import Counter, OrderedDict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    '''
    Create a hash map with key and values, such that key 
    represent the value in nums, and value represent the count
    finally return iterate through the dict uptill k elements
    '''
    
    count = (Counter(nums))
    comms = count.most_common()
    print(comms)
    temp = []
    for i,j in comms:
        if k <= 0:
            break
        else:
            k -= 1
            temp.append(i)
    
    return temp
a = [3,0,1,0]
# print(topKFrequent(a, k=1))


def topKFrequent( nums, k):
    counts = Counter(nums)
    result = []

    for _ in range(k):
        max_key = max(counts, key=counts.get)
        print(max_key)
        result.append(max_key)
        del counts[max_key]

    return result

print(topKFrequent(nums=a,k=2))


    
    