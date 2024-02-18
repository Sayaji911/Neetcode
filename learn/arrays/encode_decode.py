"""
Input: ["lint","code","love","you"]
encode to "lint:;code:;love:;you"

then decode to this 
["lint","code","love","you"]

___________________________________________________
Encoding steps

step 1 : iterate through the array
step 2 : pop each element from the array
step 3 : check if the array is empty
step 4 : if the array is not empty 
        then attach the ":;" this next to the ele
        else just attach the word to the array
________________**********_________________________

___________________________________________________
Decoding steps

step 1 : create a temp variable
step 2 : iterate and check each letter in string
step 3 : if string is alpha then add the char in 
         temp and keep adding untill it is alpha
         else if it is ":" then append the temp 
         var to a list
step 4 : increment the iterator         
--------------**********---------------------------

# """
# import random
# from typing import List


# class Solution:
#     def encode(self, strs: List):
#         i = len(strs) - 1
#         final = ""
#         while strs:
#             word = strs.pop(i)
#             if strs:
#                 if word == ":":
#                     temp = ":;:" + word
#                 else:
#                     temp = ":;" + word
#                 final = temp + final
#             else:
#                 final = word + final
#             i -= 1
#         return final

#     def decode(self, str):
#         # write your code here
#         op = []
#         word = ""
#         for i in range(0, len(str)):
#             b = str[i]
#             if str[i] == ";":
#                 op.append(word)
#                 word = ""
#             else:
#                 if str[i] == ":" and str[i + 1] == ":":
#                     if word == ":":
#                         continue
#                     word = word + str[i]
#                 else:
#                     if str[i] != ":":
#                         word = word + str[i]
#         op.append(word)
#         return op


# # s = Solution()
# # print(s.decode("we:;say:;:::;yes"))


# class Solution1:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """

#     def encode(self, strings):
#         res = ""

#         for word in strings:
#             res += word + ":" + ";"
#         return res

#     def decode(self, encoded_string):
#         return encoded_string.split(";")


# s = Solution1()
# a = ["lint", "code", "love", "you"]
# print(s.encode(a))


def encode(k: list):
    """
    convert list into str with seperatoR
    """

    res = ""

    for word in k:
        res += str(len(word)) + "#" + word
    return res


def decode(k: str):
    """
    convert str to list again
    """
    temp = []
    i = 0
    while i < len(k):
        j = i
        while k[j] != "#":
            j = j + 1

        length = int(str(k[i:j]))
        word = k[j + 1 : j + 1 + length]
        temp.append(word)

        i = j + 1 + length  
    return temp


print(decode(k="6#sayaji4#test7#nameson"))


# print(encode(k=["sayaji", "test", "nameson"]))
