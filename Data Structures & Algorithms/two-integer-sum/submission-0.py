"""
Understand:
- Input is an array of integers and one target integer
- We need to find 2 integers in the array whose sum is the target integer
- Array is all integers, no strings but can have 0
- If no pair available, return -1
- But only ONE pair will satisfy the condition
- Return is INDECES, not the actual number
- return the integer

Match:
- Arrays
- Dictionaries

Plan:
- Create a dictionary
- Loop through the array
- Subtract every number from the target number and look for that complement in the dictionary
- If the complement is present, you found your pair, return the indeces
- Else keep going
- Once out of the loop, just return -1

Implement:
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7

        my_dict = defaultdict(int)
        num_length = len(nums) # 4

        for index in range(0, len(nums)): # 1
            number = nums[index] # 4
            complement = target - number # 7 - 4 = 3

            if complement in my_dict: # true
                return [my_dict[complement], index] # [0, 1]

            my_dict[number] = index # {3: 0, }

        return -1
"""
Review:
- Done in comments

Evaluate:
- Time: O(n) to parse through every number in the nums array
- Space: O(n) where n is the size of the array because of a new dictionary used
"""     