'''
Understand:
- Given a list of integers
- And a target integer
- 2 of the integers add up to the target
- Find the 2 integers in the list and return their indeces

- Input:
    - List of integers
    - Target

- Output:
    - List of two integers (indeces of the number)
    - The two integers cannot be the same i != j

Questions:
- Guaranteed that nums only has integers? Yes, only integers, no strings or decimals/float
- No need to worry about multiple combinations of the number
- What if there are no numbers? Return [-1, -1]
- empty list? return [-1, -1]
- Does the order of returning the indeces matter? Yes, return the smaller index first

Match:
- Array/List problem

Plan:
Brute Force:
- Nested loop
- Start at one integer (i), look at all integers after that (i+1, i+2...)
- Add the sum, compare to target
- Whenever you find the combination, return the index

More optimal:
- Target never changes
- Loop through every number, subtract it from the target
- Search for the complement
- Convert nums to set (searching within the set will give me the other number in O(1) time)
- But set will not give me the index
- Number + index, nice to have O(1) lookup time for the complement
- Dictionary
    - key: number
    - value: index
- For every number, we calculate the complement, if it exists, we return the index of the number and its complement's index from the dictionary
- O(1) lookup time
- Outside the loop, we return [-1, -1]

Implement:
'''

# nums = [4,5,6], target = 10
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dictionary = defaultdict(int)
        # {
        #   4 : 0,
        #   5 : 1,
        #   
        #}

        for index, number in enumerate(nums): # 2, 6
            complement = target - number # 10 - 6 = 4

            if complement in complement_dictionary: # True
                complement_index = complement_dictionary[complement] # 0
                return [complement_index, index] # 0, 2
            
            complement_dictionary[number] = index

        return [-1, -1]

'''
Review:
Done in comments

Time:
- Worst case complexity: O(n), parse through every number in the list
Space:
- Worst case: O(n), dictionary is extra space for every number
'''
        