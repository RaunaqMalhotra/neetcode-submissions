"""
Understand:
- Start with a list of strings
- Make them one string with the encode function
- Decode the string by sending the encoded string as an argument and return the original list of strings
- String can be empty
- String can have any character like , ; {space} etc.
- Input: List of strings
- Output: List of strings (after decoding)

Match:
- String
- Arrays/Lists
- ASCII

Plan:
strs = ["Hello", "", "World"]
To encode, we're gonna come up with our own delimiter which is length#
So for "Hello", we will use 5# in the encoded string
After concatenation, it will look like 5#Hello0#5#World

To decode, we will read the string. We know it will start with a number
We will keep reading character by character until we reach a hash
As soon as we do, we will take the substring starting from the following index until the length before the #
Once we get the word, we will add it to the output decoded list
We will then jump the indeces to start at the next word
Even if there is a number# in the middle of the world

Implement:
"""
class Solution:

    # strs = ["Hello", "", "Wor3#"]
    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # 5#Hello0#5#Wor3#

        for word in strs: # "World"
            length = len(word) # 5
            encoded_string += f"{length}#{word}" # 5#Wor3#
        
        return encoded_string # 5#Hello0#5#Wor3#

    # 5#Hello0#5#Wor3#
    def decode(self, s: str) -> List[str]:

        decoded_strs = [] # ["Hello", "", "Wor3#"]
        length_encoded = len(s) # 16
        
        str_current_length = ""
        index = 0

        while (index < length_encoded): # 16 < 16 false
            character = s[index] # #

            if character == "#": # # == # true
                int_current_length = int(str_current_length) # 5
                str_current_length = ""

                if int_current_length == 0: # false
                    decoded_strs.append("") # append ""
                
                else:
                    start = index + 1 # start = 10 + 1 = 11
                    end = index + int_current_length + 1 # 10 + 5 + 1 = 16
                    # end is the last index of the word which needs to be included in the current word, hence the +1
                    current_word = s[start:end] # s[2:7] = Wor3#
                    decoded_strs.append(current_word) # append "Wor3#"
                
                # Next number starts after the end of the last word 
                # i.e. +1 index
                index += int_current_length + 1 # index = 10 + 5 + 1 = 16
            else:
                str_current_length += character # 5
                index += 1 # index = 9+1 = 10

        return decoded_strs

"""
Review:
- done in comments

Evaluate:
Time:
- Encode: O(m) where m is the length of strs
- Decode: O(m) because the while loops goes through the same
number of words in the encoded string as the original list

so, final time is O(m)

Space:
- encoded string = O(n + 2*m) where n is the sum of lengths every word 
    and 2*m because of 2 extra characters for the length of each string 
    (number#)
- decoded strs = length of strs = O(m)

so, final space is O(2m+n) OR O(m+n)
"""
