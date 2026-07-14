"""
Understand:
- Input is a string
- String only consists of open and close brackets
- Do I need to take care of other characters in the string? No
- Can the string be empty? yes. Is that a valid string? yes
- Can string have empty spaces?
- Check if the string is valid or not by following the three conditions on the left
    - every opening bracket should have a closing bracket of the same tme
    - vice versa
    - And they should be closed in the same order they were open in
- Return type is boolean
- Also, if the string is of odd length, that means there is a 
    singular bracket not part of a pair, i.e. return False

Examples of invalid string:
((())
(
[])
{[(])}

Match:
- Arrays and stacks

Plan:
- Declare an empty stack
- Go through every character in the string
- If it is an open bracket, add it to the stack
- If it is a closed bracket,
    - check if the stack is empty. If yes, that means no open brackets i.e. return False
    - if stack exists, pop the most recent element
    - if most recent open bracket matches the closed bracket, continue, else return False
    - This takes care of the order of opening and closing
- In the end, check if stack is not empty. If it is not, that means there is an un-closed open bracket, return false
- In the end return True after all checks
"""

class Solution:
    # [(])
    def isValid(self, s: str) -> bool:

        length = len(s) # 4

        if length  % 2 == 1: # valid string will always be even (false)
            return False

        stack = [] # ["[", "("]
        open_set = set(["{", "(", "["])
        close_set = set(["}", ")", "]"])
        open_close_dictionary = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        for character in s: # ]
            if character in open_set: # false
                stack.append(character) 
            
            elif character in close_set: # true
                if not stack: # stack is empty (false)
                    return False
                
                current_open = stack.pop() # "("
                if character != open_close_dictionary[current_open]: # true
                    return False # returns False

        if stack:
            return False

        return True

"""
Review:
- done in comments

Evaluate:
Time = O(n), it goes through the entire string character by character
Space = O(n) because of the stack. In worst case, the entire string is open characters so len(stack) == len(string)

where n is the length of the input string
"""
        