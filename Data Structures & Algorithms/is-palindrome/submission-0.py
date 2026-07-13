"""
Understand:
- Input is a string
- Determine if the given string is a palindrome
- Palindrome: string which has the same characters backwards as it does when you read it forward
- This applies only to ALPHANUMERIC CHARACTERS i.e. letters and numbers only, regardless of the case
- All other characters are to be ignored
- So checking if the characters from the start is the same as from the back until you get to the middle
- If everything is the same, then it's a palindrome
- Otherwise it's not

- Return type after checking is boolean (true/false)
- String can have any ASCII characters? Yes
- Can the string be empty? Is that a palindrome if yes?
- Is a string of length one a palindrome? Yes coz same characters forward and backward
- Time or Space restrictions I should follow?

Match:
- Two pointer approach
- Strings
- ASCII values (a-z : 97-122 and 0-9: 48 to 57)

Plan:
- Convert string to lowercase since palindrome strings are case insensitive
- Declare two pointers, one starts at index 0 and another starts at index len-1
- while loop (first_pointer <= last_pointer)
- take both characters at the two indeces and make sure they're alpha numeric
- If not, i update the pointer which is not and then the loop compares again
- If both alphanumeric, I check if they're equal
- If not equal, return False
- Continue checking until while condition is false
- Return true at the end

Implement:
"""
class Solution:
    # "Was it a car or !a cat I saw?"
    def isPalindrome(self, s: str) -> bool:

        s = s.lower() # # "was it a car or !a cat i saw?"
        first = 0 # 0
        last = len(s) - 1 # 29

        while (first <= last): # 5 < 22? true

            first_char = s[first] # t
            ascii_first = ord(first_char) # 116

            last_char = s[last] # t
            ascii_last = ord(last_char) # 116

            if not (47 <= ascii_first <= 56 or 97 <= ascii_first <= 122): # false
                first += 1 # 4
                continue

            if not (47 <= ascii_last <= 56 or 97 <= ascii_last <= 122): # false
                last -= 1 # 22
                continue

            if not (first_char == last_char): # false
                return False
            
            first += 1 # 5
            last -= 1 # 23
        
        return True

"""
Review:
- Done in comments

Evaluate:
- Time: O(n), goes through the entire length of the string
.lower() is also O(n)

O(n) + O(n) = O(n) time

- Space: No extra space used, only variables so space is O(1)
"""
        