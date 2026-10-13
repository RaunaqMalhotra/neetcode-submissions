'''
Understand:
- Given an array nums with some amount of integers
- Input: List/Array
- If the array has any element that appears twice in the list/array

- Look at all the elements
- If duplicate element, return True, otherwise return False
- Output: boolean

- Integer array so elements can also be negative

Question:
- Can array be empty? Return false (no duplicate element)
- Return true for even one duplicate value
- Non-integer elements? No
- Are the arrays always sorted? No

Match:
- Array
- Sets

Plan:
Brute:
- Nested loop
- Start at one element
- Look at all of the elements after that
- If any of the following elements match the element from the outer loop, return True, else False after the nested loop
- Nested loop: O(n^2) lookup

Sets (constant lookup time):
- Create a set
- Loop through the array once
- If element already in set, return true (for duplicates)
- Otherwise add it to the set
- Return False outside the loop
- One loop: O(n) lookup
- Space: O(n) because of the set


POINTERS DO NOT WORK (EXAMPLE [1, 2, 1, 3])

Even better way (in terms of space):
- Two pointers
- left at 0 index and right at last element index (len - 1)
- While left < right
- compare the values at left and right
- left + 1 & right - 1
- if left element == right element, return True
- else False outside the while loop
- Time O(n) BUT Space O(1)

Implement:
'''
# nums = [1, 2, 1, 3]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()

        for number in nums:
            if number in unique_set:
                return True

            unique_set.add(number)

        return False

'''
Review:
Done in comments

Evaluate:
- Time: O(n), loop through all the elements of the list once in worst case
- Space: O(n), extra set with all elements of list
'''