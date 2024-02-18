def isValidAnagram(s : str, t = str) -> bool:
    # return sorted(s) == sorted(t)  
    count = {}
    if len(s) == len(t):
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        for j in t:
            if j in count:
                count[j] -= 1
        
        for k in count.values():
            if k != 0:
                return False
        return True


from collections import Counter
def isValidAnagram2(s : str, t = str) -> bool:
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"

print(isValidAnagram2(s,t))



