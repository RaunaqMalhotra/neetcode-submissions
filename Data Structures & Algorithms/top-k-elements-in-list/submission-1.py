'''
Understand:
- Given a list of repeating or non-repeating integers
- Also given a value "k"
- We have to return "k" number of most frequently appearing elements
- Input:
    - List of integers
    - k (which is the length of our final list we return i.e. number of unique elements which appear most frequently)

- Output: List of unique integers

Questions:
- Check for edge case of empty list with non-zero k? No
- Check for non-integer elements in list? No
- Can k be 0? No
- Can k be greater than the number of unique elements in the list? No
- What if there are four 3's, four 2's, four 1's, and two 0's? And k is 2? Which two numbers do I return?
- Array is not sorted, I'm assuming? Frequency of a number can be anywhere in the list? yes, non-sorted array

Match:
- Since we have to keep track of number AND its frequency, dictionary would be great
- Arrays for initial list

Plan:
- Go through the list
- Create a dictionary with number and its corresponding frequency
    - key: number
    - value: frequency
    OR  
    - key: frequency 
    - value: list of numbers in that frequency
- Sort the dictionary by its keys/values
- return the numbers with the highest frequency up until "k"
- O(n log n) for sorting where n is the number of unique elements in the list, worst case if all elements are unique, then n is the size of list

More Optimal O(n) solution:
- Bucket sort
- Go through the list and make the dictionary like before
    - keys: number
    - values: frequency
- Create a bucket list of lists the size of "nums", that's the maximum number of unique elements in the list
- Go through the dictionary, add the number to a list and add that list to the corresponding frequency in the bucket

For example:
nums = [1,2,2,3,3,3]
1 : 1
2 : 2
3 : 3

create a bucket list of size 6 (length of list + 1)
[[], [1], [2], [3], [], [], []]
go through the dictionary, and add numbers to the list corresponding to the bucket
3 goes in bucket 3
2 goes in bucket 2
1 goes in bucket 1

Loop back from the list and add the unique elements to the final result until final result's length == k

return the final result

Implement:
'''
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency_dictionary = defaultdict(int)
        len_nums = len(nums)

        for number in nums: # O(n)
            frequency_dictionary[number] += 1

        bucket = [[] for _ in range(len_nums+1)]

        for key, value in frequency_dictionary.items(): # O(n)
            bucket[value].append(key)

        for index in range(len(bucket)-1, -1, -1): # O(n)
            current_list = bucket[index]
            for element in bucket[index]:
                result.append(element)
                if len(result) == k:
                    return result
        
        return result

'''
Evaluate:
Time: O(n) because even though there is a nested loop, at most I am going through all n elements in the second loop. So it's actually O(n + n) = O(2n) = O(n)

Space: O(n) for the dictionary and the bucket list
'''