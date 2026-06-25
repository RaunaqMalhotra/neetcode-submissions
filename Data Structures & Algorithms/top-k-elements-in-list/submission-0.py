"""
Understand:
[1, 2, 2, 3, 3, 3]
- This is a sorted array 
- BUT not required that all arrays will be sorted
- Input is an array of integers and an integer k
- In the array, count the number of each element
- Then return the elements with the "k" highest frequencies
- So, in the above example, 1 appears 1 time, 2 appears 2 times, and 3 appears 3 times so the top k (2) elements are 2 and 3
- No empty arrays, always integers
- k will always be an integer as well
- k will not exceed the number of unique elements in the array

Match:
- Dictionary to keep count
 - key is the element, value is the count
- Array of arrays to keep frequency of the elements

Plan:
- Declare a default dictionary and an empty array of arrays of size n+1
- Go through nums and count the number of each element
- Go through the dictionary
- Get each element and its count/frequency
- At the index corresponding to the element's frequency, append the element to the array at that index
- Start from the end of the array and return the top k number of elements

Implement:
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,2,2,3,3,3]
        count_dictionary = defaultdict(int) # {}
        length = len(nums) # 6
        freq_array = [[] for _ in range(length+1)] # [[], [], []...]
        output = [] # []

        for number in nums: # 3 O(n)
            count_dictionary[number] += 1 # {1: 2, 2: 2, 3: 3}

        for number, frequency in count_dictionary.items(): # 1, 1 O(n)
            freq_array[frequency].append(number) # [[], [], [1, 2], [3], [], [], []]

        index = length # 6
        while (k > 0): # k = 0 and index = 1 (loop ends) # O(k) which is constant
            current_array = freq_array[index] # [1, 2]
            for element in current_array: # 1 O(n)
                output.append(element) # output = [3, 1]
                k -= 1 # k = 0
                if k == 0: # true
                    break
            
            index -= 1 # 1

        return output

"""
Review:
- Done in comments

Evaluate:
- Time Complexity:  O(n)
- Space Complexity: O(n)
    - O(n) for dictionary
    - O(n+1) for array of arrays
        - the entire array of arrays will at most hold n elements 
            so the total would be O(n+1) + O(n) = O(n)
"""
        