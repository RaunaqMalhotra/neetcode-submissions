"""
Understand:
- Input is an array of integers, it can be negative or positive
- For every integer, I need to calculate a product value of every integer in the list EXCEPT that integer in that index
- Output is a list of calculated integers
- Output list length will be of the same length as the original input list
- Input length will have at least 2 numbers, this cannot work with an empty list or 1 integer

Match:
- Prefix/Postfix in List/Array

Plan:
- Make a list of products of integers BEFORE the said integer (prefix)
- Make a list of poducts of integers AFTER the said integer (postfix)
- Multiply both prefix and postfix lists to create the final output list

[1, 2, 4, 6]

Prefix list = [1, 1, 1*2, 1*2*4]
Postfix list = [2*4*6, 4*6, 6, 1]

Final output    = [1*2*4*6, 1*4*6, 1*2*6, 1*2*4*1]
                = [48, 24, 12, 8]

Implement:
"""
class Solution:
    # nums = [2, 2, 4, 6]
    # prefix = [1, 2, 4, 16]
    # postfix = [48, 24, 6, 1]
    # output = [48, 48, 24, 16]
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        output = []

        # nums = [2, 2, 4, 6]
        # output = [1, 2, 4, 16]
        current_prefix = 1
        for index, number in enumerate(nums):
            if index > 0: # 3 > 0 true
                current_prefix *= nums[index-1]
            
            output.append(current_prefix)

        
        # nums = [2, 2, 4, 6]
        # ouptut = [1, 48, 24, 16]
        current_postfix = 1
        for index in range(len_nums-1, -1, -1): # 0
            if index < len_nums-1: # 0 < 3 true
                current_postfix *= nums[index+1] # 24 * nums[1] = 24*2 = 48

            output[index] *= current_postfix # 1*48 = 48

        return output

"""
Review:
- done in comments

Evaluate:
- Time complexity: O(n) for first loop and O(n) for second loop
- Final time: O(n)

- Space complexity: O(n) for only the output list used
"""        