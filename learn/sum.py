
import re


def hasPairWithSum(array : list, sum : int) -> bool:
    """
    This function return true if the array contains the numbers to create the sum
    """

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == sum:
                return True

    return False

def hasPairWithSum2(array: list, sum : int) -> bool:
    myset = set()
    for ele in array:
        if ele in myset:
            return True
        else:
            myset.add(int(sum - ele))
    return False




print(hasPairWithSum2([1,10,3,3], 6))

