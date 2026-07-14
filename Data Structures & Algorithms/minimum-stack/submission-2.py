"""
Understand:
- We have to design a stack function class
- Basically, replicate how a stack behaves (LIFO last in first out)
- To do that we have to implement different functions to replicate the stack
- However, in this version of the stack, we also have to keep track of the minimum element
- There is a function called "getMin" which gets the least element of the stack
- The stack will consist of integers only
- MinStack() to initialize and declare the stack
- push, pop, top as standard functions to add, remove, and peek at the top element respectively
- Also, a big caveat is that every single function should be O(1) time
- No limitations on space, but time is constant
- What if pop/top/getMin is called on an empty stack? Should I return -1?
    (not required right now)
- Will function calls always be in the right order?

Match:
- Lists
- Integers

Plan:
- So, since there are no space restrictions and time needs to be O(1)
- We can use another list to keep track of the minimum elements (min stack)
- So we initialize two lists - one for the normal stack, one for minimum
- Elements will only be added to min which are smaller than the top most element
- this will help us keep track of the most current minimum element
- push will add the element in the normal stack
    - if the element is smaller than or equal to the topmost element of the min stack, then we add the element to the min stack as well
- pop will remove the top most element in normal and if it is the same as topmost of minimum, that will also be removed
- top will just simply return the last element of the normal stack
- getMin will just simply return the last element of the minimum stack

Implement:
"""

#Input: 
# ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
class MinStack:

    def __init__(self): # getMin
        self.stack = [] # [1, 2]
        self.min_stack = [] #[1]

    def push(self, val: int) -> None: # called with 0
        self.stack.append(val) # append 0
        length_min = len(self.min_stack) # 1

        if length_min == 0: # false
            self.min_stack.append(val) # append 1
        # I know python allows me to do self.min_stack[-1] 
        # but I just wanted to make sure logically it makes sense
        elif val <= self.min_stack[length_min - 1]: # 0 < min[0] = 0 < 1? true
            self.min_stack.append(val) # append 0
            
    def pop(self) -> None: # called
        length_stack = len(self.stack) # 3
        length_min = len(self.min_stack) # 2

        # stack[2] == stack[1]? 0 == 0? True
        if self.stack[length_stack - 1] == self.min_stack[length_min - 1]:
            self.min_stack.pop() # remove 0 from min

        self.stack.pop() # remove 0 from stack

    def top(self) -> int: # called
        length = len(self.stack) # 2
        return self.stack[length - 1] # stack[2-1] = stack[1] = 2

    def getMin(self) -> int: # called
        length_min = len(self.min_stack) # 1
        return self.min_stack[length_min - 1] # min[1-1] = min[0] = 1

"""
Review:
- Done in comments

Evaluate:
- Time is O(1), no loops, no parsing through any stacks

- Space is O(n) : O(n) for stack + O(n) for min stack
"""