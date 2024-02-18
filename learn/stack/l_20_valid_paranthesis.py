class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []


        for brack in s:
            if brack not in bracket_pairs:
                stack.append(brack)
                continue

            if not stack or stack[-1] != bracket_pairs[brack]:
                return False
            stack.pop()
        return not stack


obj = Solution()

input = "]"


print(obj.isValid(input))


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "[": "]", "{": "}"}
        stack = []
        if len(s) < 2:
            return False
        
        for brack in s:
            if brack in bracket_pairs.keys():
                stack.append(brack)
            else:
                if brack in bracket_pairs.values() and len(stack) > 0:
                    if bracket_pairs[stack[len(stack) - 1]] != brack:
                        return False
                    else:
                        stack.pop(len(stack) - 1)
                else:
                    return False    
        if len(stack) > 0:
            return False
        return True
