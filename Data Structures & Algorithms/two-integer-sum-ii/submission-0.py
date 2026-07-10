"""
Understand:
- Input is a SORTED array of integers
- Integers are in increasing order
- Cannot use additional space/data structures
- Find two such integers whose sum add up to the given target integer
- Cannot use the same element twice and there is always only ONE valid solution
- Empty array? Not applicable
- Array with only 1 number? Not applicable
- What if the array doesn't have a solution? Not applicable here, but you can return [-1, -1] in general
- The two elements returned HAVE to have indeces where first index < second index

- Return the indeces of the two numbers (return type: array of 2 integers)
INDECES START AT 1, NOT 0

Match:
- Array/List
- Two pointers

Plan:
- Have a left pointer at index 0
- Have a right pointer at the last index of the array
- Calculate sum, if sum found, return the two indeces+1 (1-indexed array)
- If sum < target, that means we need bigger numbers, so move left pointer to one space right
- If sum > target, that means we need a smaller number, so move the right pointer to one space left
- Keep moving the pointers as long as left < right (that's one condition given in the question)


This is only possible because the array is sorted so it follows an increasing order of integers
Therefore it follows an increasing order of sums

No extra space used, time estimated to be O(n) since we just parse through the array once
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # numbers = [1, 2, 3, 4] and target = 7
        left = 0
        right = len(numbers) - 1 # 3

        while (left < right): # 2 < 3? true

            current_sum = numbers[left] + numbers[right] 
            # numbers[2] + numbers[3] = 3 + 4 = 7

            if current_sum == target: # 7 == 7? true
                return [left+1, right+1] # return [2+1, 3+1] = [3, 4]

            elif current_sum < target: # 6 < 7? true
                left += 1 # 2

            elif current_sum > target:
                right -= 1
        
        return [-1, -1]

"""
Review:
- Done in comments

Evaluate:
Time:
    - O(n-1) = we start at 0 and go until the end of the array (just -1 before right)
So finally, time is O(n)

Space: O(1) because no additional space is used
"""
        