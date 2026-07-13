"""
Understand:
- Given an integer array nums
- Not sorted (Input is a list of integers)
- Return list of lists
- Each sublist will have 3 numbers whose sum will add up to 0
- However, you cannot use the number at the same index twice
- Those 3 numbers that you return will have 3 unique indeces, i, j_left, and k_right
- You can use the same number in another list, j_leftust not in the same list
- Also, nums minimum length is 3
- There can be an array with no solution at all

Match:
- Indeces and pointers
- Arrays
- Can also use hashmaps (And apply the two sum methods for each number)
- BUT, space has to be O(1)

Plan:

[-1, 0, 1, 2, -1, -4]
[-4, -1, -1, 0, 1, 2]

Sort the array
Then for every number, do the two pointer solution for the two sum
i.e.
start at index+1 and last index
if sum of all numbers < 0, then we move left pointer to the right since we want a bigger number to get closer to 0
if sum of all numbers > 0, then we move right pointer to the left since we want a smaller number to get closer to 0
if sum of all numbers == 0, then add it to the list

Since the initial loop goes through the list once
You don't need to check_right previous numbers since all permutations 
with the previous numbers have already been tested
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-1, 0, 1, 2, -1, -4]
        
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        output = [] # []
        length_nums = len(nums) # 6

        # Only iterate till the third last number 
        # (so len-2 since end of range is exclusive)

        # [-4, 2, 2, 0, 1, 2]
        for i, number in enumerate(nums): # 0
            if i > 0 and number == nums[i-1]: # No need to look at repeated numbers
                continue

            j_left = i + 1 # 3
            k_right = length_nums - 1 # 5

            while (j_left < k_right): # true
                three_sum = nums[i] + nums[j_left] + nums[k_right]
                # nums0 + nums3 + nums5 = -4 + 0 + 2 = -3

                if three_sum == 0: # false
                    output.append([nums[i], nums[j_left], nums[k_right]])
                    j_left += 1
                    # No need to look at repeated numbers
                    while nums[j_left] == nums[j_left-1] and j_left < k_right:
                        j_left += 1

                elif three_sum < 0: # true
                    j_left += 1
                
                elif three_sum > 0:
                    k_right -= 1

        return output

"""
Review:
- Done in comments

Evaluate:
- Time: 
1. O(n log n) for sorting
2.  O(n-2) for outer loop since it loops through numbers at indeces 0 
    to length-2 
    And O(n-1) for inner loop since it starts at either end of the list
    and loops through every number in the worst case
Total time is O(n-2)(n-1) i.e O(n^2)

- Space:
    O(1), no extra space used
    nums.sort() sorts the array in place
"""
