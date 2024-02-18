class LRUCache:
    """


    So here what I am thinking

    q1. How will we store the values ?
    a.  We can use a dictionary to store the
        key value pairs

    q2. How will we implement the get method ?
    a3.  We will the dicts get method to get the value
        if it exists or else return -1 as default


    q3. How will we implement the put method ?
    a3. We could insert the key val pair into the
        dictionary, if it already exits we can update it

    q4. How will we implement the key eviction mechanism ?
    a4.
        Alright, so lets suppose
        the capacity is 2

        we add the first pair
        then we add the 2nd pair

        lets say we also a stack which
        maints the least used keys

        when we add the pair into the cache
        we also add the key to a stack

        now this stack will be FIFO
        as we add the keys, it will
        fil the stack, once the capacity is
        reached, it will pick the first ele
        from stack and delete the key pair

        if the element is used then it will pick
        the element and put it back from the last


        if the key is deleted then it will also
        be deleted from the list

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.registry = []

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val == -1:
            return val
        self.registry.remove(key)
        self.registry.append(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.registry.remove(key)
            self.registry.append(key)
            
        else:
            if len(self.cache) == self.capacity:
                key_to_delete = self.registry[0]
                self.cache.pop(key_to_delete)
                self.cache[key] = value
                self.registry.remove(key_to_delete)

                self.registry.append(key)
            else:
                self.cache[key] = value
                self.registry.append(key)

        return None


def perform_operations(operations, values):
    result = []
    obj = None

    for operation, value in zip(operations, values):
        if operation == "LRUCache":
            obj = LRUCache(*value)
            result.append(None)
        elif operation == "put":
            result.append(obj.put(*value))
        elif operation == "get":
            result.append(obj.get(*value))

    return result


# Example usage
# operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

operations = ["LRUCache", "put", "put", "put", "put", "get", "get"]

values = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

output = perform_operations(operations, values)
print(output)
