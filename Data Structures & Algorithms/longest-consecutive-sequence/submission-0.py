"""
Understand:
- Input is a list of integers (positive and negative)
- Not sorted, in random order
- Find the longest consecutive sequence of numbers i.e 1, 2, 3, 4
- Numbers can be out of order
- Time has to be O(n), so sorting is out of the question since best sorting algorithm (merge sort) is O(n log n)
- What do I return if the list is empty? 1 or 0? I will return 0
- Output will be an integer (the longest consecutive sequence)

Match:
- List/Arrays
- Set

Plan:
- We'll first put all numbers in a set because it will be easier to check if consecutive numbers exist in the set or not
- Set lookup time is O(1)
- Set will also get rid of duplicate elements since that is not necessary here


(2,20,4,10,3,4,5)
- 2 (is -1 in the set? No, so start at 2 and keep a counter)
- is +1 (3) in the set? yes, keep going until you reach 5
- Now in this example, since 5 is the last number, we check if +1 for 5 exists or not,
- Since it doesn't, we stop and move to the next element

Implement:
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # (2,20,4,10,3,4,5)
        num_set = set(nums)
        answer = 0 # 0

        for number in nums: # 5
            counter = 1
            prev = number - 1 # 4
            next_num = number + 1 # 3

            if prev in num_set: # true
                continue
            
            while (next_num in num_set): # 11 in set false
                counter += 1 # counter = 4
                prev = number # prev = 4
                number = next_num # number = 5
                next_num = number + 1 # next_num = 6

            answer = max(answer, counter) # max(4, 1) = 4

        return answer

"""
Review:
- Done in comments

Evaluate:
- Time: O(n)
    - for loop goes through every number O(n)
    - set lookup is O(1)
    - While loop goes through the entire sequence only once (it won't repeat for numbers which have a -1 in the set) so O(1)

- Space: O(n) for the extra set of numbers
"""     