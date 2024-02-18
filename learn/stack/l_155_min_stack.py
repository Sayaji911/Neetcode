from typing import Any

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Given calls for the object
calls = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [[], [-2], [0], [-3], [], [], [], []]

# Initialize the MinStack object
obj = None
outputs = []

# Iterate through each operation
for call, value in zip(calls, values):
    if call == "MinStack":
        obj = (
            MinStack()
        )  # Initialize the MinStack object outputs.append(None)  # No output for initialization
    elif call == "push":
        obj.push(value[0])  # Call the push method with the provided value
        outputs.append(None)  # No output for push operation
    elif call == "pop":
        outputs.append(obj.pop())  # Call the pop method and store the output
    elif call == "top":
        outputs.append(obj.top())  # Call the top method and store the output
    elif call == "getMin":
        outputs.append(obj.getMin())  # Call the getMin method and store the output

# Print the outputs
print(outputs)
