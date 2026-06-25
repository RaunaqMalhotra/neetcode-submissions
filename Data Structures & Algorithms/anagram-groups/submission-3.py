"""
Understand:
- What are anagrams? Two strings, with the same letters, but arranged in any order
    - This means that the lengths of the two strings have to be the same
- strs can have empty strings within
- In that case, just group and return the empty strings together
- Input: List of strings
- Output: List of lists of strings



strs = ["act","pots","tops","cat","stop","hat"]
hat
[["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

Match:
- An array of 26 numbers where a number indicates the number of letters in the word
- Dictionary where every word is stored in an array
- Key is the array of numbers and value is the array of words/anagrams

Plan:
- For every word, make an array of size 26 with 0s
- For every character in the word, the corresponding position in the array would be +1
- Use ASCII values to convert letter into number
- Once the array is changed, put it in the dictionary as tuple with the corresponding word in the value array
- Go through the dictionary and return all arrays

Implement:
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]

        output = []
        anagram_dictionary = defaultdict(list) # O(m) space where m is the number of strings

        for word in strs: # Time = Length of str array O(m)

            word_array = [0] * 26

            for letter in word: # Time = length of the longest word O(n)

                index = ord(letter) - ord("a")
                word_array[index] += 1
            
            anagram_dictionary[tuple(word_array)].append(word) #{[1,0,1,0,0,...]: ["act", "cat"]}

        for key, value in anagram_dictionary.items():
            output.append(value)

        return output



"""
Review:
- Done in comments

Evaluate:
- Time: O(m*n) where m is the number of strings and n is the length of the longest string
- Space: O(m) where m is the number of strings (dictionary for each unique word)
"""
        