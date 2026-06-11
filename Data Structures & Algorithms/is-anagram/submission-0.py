'''
Understand:
- What are anagrams? 
    Two words containing the same letters but the order of the letters can be different
- This means that the two words have to have the same length to be an anagram
- Count of the letters matters
- Can the strings be empty? If yes, are empty strings anagrams, i.e. return True?
- Input: string
- Return: boolean

Match:
- Could sort and then compare the sorted strings
OR
- Could do a hashmap with count of each letter for each string

Plan:
- Check length, if different, return False
- Go through each string and create a hashmap/dictionary for both
- Compare the two hashmaps, if the values and keys both match, then it is an anagram
- If the match fails anywhere, return False, else at the end, return True

Implement:
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # s = racecar ; t = carrace
        length_s = len(s) # 7
        length_t = len(t) # 7

        dict_s = {} # {r : 2, a : 2, c : 2, e : 1}
        dict_t = {} # {c : 2, a : 2, r : 2, e : 1}

        if length_s != length_t: # false O(1)
            return False
        
        for letter in s: # r O(n)
            if letter in dict_s: # true
                dict_s[letter] += 1
            else:
                dict_s[letter] = 1 

        for letter in t: # e O(n)
            if letter in dict_t: # false
                dict_t[letter] += 1
            else:
                dict_t[letter] = 1

        for key, value in dict_s.items(): # e, 1 O(n)
            if key not in dict_t: # false O(1)
                return False
            
            if dict_t[key] != value: # dict_t[e]=1 != 1 ==> false
                return False

        return True # returns True

"""
Review:
- Done in comments

Evaluate:
- Runtime = O(n) where n is the length of the longer string (loops for each string)
    - Dictionary lookup time is constant
- Space = O(n) where n is the length of the longer string (two dictionaries)
"""
        