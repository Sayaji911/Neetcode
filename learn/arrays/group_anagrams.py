# from collections import Counter
from typing import List
# def groupAnagrams(strs: list) -> list:
#     """ 
#     iterate through the array and
#     for every element in array check
#     for an anagram using a function inside the array
    
#     and then append the word with the functions result
#     array
#     """
#     def _isAnagram(ele: str) -> None:
#         temp = []
        
#         for k in range(0,len(strs)):
#             if Counter(ele) == Counter(strs[k]):
#                 temp.append(strs[k])
                

#         pairs.append(temp)

#         [strs.remove(t) and print(f"Removed: {t}") for t in temp]

#         temp = []
        
#     pairs = []
#     for ele in strs:
#         print(strs.index(ele))
#         _isAnagram(ele=ele)
    
#     return pairs
# strs = ["eat","tea","tan","ate","nat","bat"]      
# # print(groupAnagrams(strs))



# from collections import defaultdict

# def groupAnagrams2(strs):
#     anagrams_dict = defaultdict(list)

#     for word in strs:
#         # Use the sorted tuple of characters as a key
#         sorted_key = tuple(sorted(word))
        
#         anagrams_dict[sorted_key].append(word)

#     # Convert the values (lists of anagrams) to a list
#     print(anagrams_dict)
#     grouped_anagrams = list(anagrams_dict.values())

    # return grouped_anagrams

# Example usage:
# strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams2(strs1))

# strs2 = [""]
# print(groupAnagrams2(strs2))

# strs3 = ["a"]
# print(groupAnagrams2(strs3))

def groupAnagrams3( strs: List[str]) -> List[List[str]]:
    dic={}
    for word in strs:
        sorted_word="".join(sorted(word))
        if sorted_word not in dic:
            dic[sorted_word]=[word]
        else:
            dic[sorted_word].append(word)
    print(dic)
    return dic.values()


# # Example usage:
# strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams3(strs1))

# strs2 = [""]
# print(groupAnagrams3(strs2))

# strs3 = ["a"]
# print(groupAnagrams3(strs3))



from typing import List

def groupAnagrams( strs: List[str]) -> List[List[str]]:
    """
    the logic is to iterate through the strs, sort it and then store it
    as a key and and the unsorted as the value in a list, 

    finally print all values as a list of list
    """
    
    word_dict = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]
    
    return list(word_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))