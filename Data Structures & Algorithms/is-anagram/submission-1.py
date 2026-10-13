'''
Understand:
- Two strings
- Look at the strings and figure out if they are anagrams
- Anagrams: Two strings with the same letters in same frequency (count is important), arranged in different ways

racecar and carrace
r = 2
a = 2
c = 2
e = 1

c = 2
a = 2
r = 2
e = 1
same letters, same frequency, so return True (they're anagrams)
If length is not the same, they're not anagrams (frequencies differ)

Input: Two strings
Output: boolean

Question:
- What if strings are empty? Both - true, one - false
- Strings can have any characters, not just letters? Yes
- does case matter? Is a == A? Case does not matter, a == A (make everything lowercase)

Match:
- Dictionaries (letter AND corresponding counts are important)
- Dictionaries give a constant lookup for comparison

Plan:
Brute force:
- Sort both strings, compare them and return true/false
- merge sort: O(n log n)

Better O(n):
- compare lengths, if not equal, return False
- with dictionaries
- loop through both strings
- add letter + frequency in the dictionary

- 2 dictionaries (one for s, one for t)
- go through one dictionary
- check if key exits in the other dictionary
- then check if value is the same
- if not, return False
- otherwise return True at the end of the comparison

Implement:
'''
from collections import defaultdict

# s = "racecarr", t = "carracee"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s) # 7
        length_t = len(t) # 7

        if length_s != length_t: # false
            return False

        dictionary_s = defaultdict(int) # {r : 3, a : 2, c : 2, e : 1}
        dictionary_t = defaultdict(int) # {c : 2, a : 2, r : 2, e : 2}

        for character in s: # r
            dictionary_s[character] += 1

        for character in t: # e
            dictionary_t[character] += 1
        
        for key, value in dictionary_s.items(): # r, 3
            if key not in dictionary_t or dictionary_t[key] != value: 
                # false or 2 != 3 (true)   
                return False # return false

        return True

'''
Review:
Done in comments

Evaluate:
Time: O(s+t) where s and t are the lengths of the strings (loop through each once)
Space: O(s+t) because of the two dictionaries of s and t length each
'''
