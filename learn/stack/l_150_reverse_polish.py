import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        lets iterarte over the token

        and place each token in a stack

        if the token is a element and the last

        two ele are token then we pop last two

        items, perform operation on them and put it

        back on the stack.
        """

        result = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }
        for tk in tokens:
            if tk in ops.keys():
                b, a = int(result.pop()), int(result.pop())
                op = ops.get(tk)
                res = op(a, b)
                print(res)
                result.append(res)
            else:
                result.append(tk)
        return result


obj = Solution()
print(
    obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)
