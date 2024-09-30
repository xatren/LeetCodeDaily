class CustomStack:
    def __init__(self, maxSize):
        """
        Initialize the stack with maximum size.
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.size = 0

    def push(self, x):
        """
        Push an element onto the stack if it's not full.
        :type x: int
        :rtype: None
        """
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1

    def pop(self):
        """
        Pop and return the top element from the stack.
        :rtype: int
        """
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        return -1

    def increment(self, k, val):
        """
        Increment the bottom k elements of the stack by val.
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, self.size)):
            self.stack[i] += val

# stk = CustomStack(3)
# stk.push(1)
# stk.push(2)
# print(stk.pop())  # Output: 2
# stk.push(2)
# stk.push(3)
# stk.push(4)
# stk.increment(5, 100)
# stk.increment(2, 100)
# print(stk.pop())  # Output: 103
# print(stk.pop())  # Output: 202
# print(stk.pop())  # Output: 201
# print(stk.pop())  # Output: -1