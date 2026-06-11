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
- Dictionary for every unique word (act, pots, hat)
- Can also do sorting but that will take a lot of time
- Match the key and value for dictionary

Plan:
- Go through every word
- Create a dictionary for that word
- If there is already something in the output, loop through the first word of the output
- Match the current word's dictionary with the first word's dictionary
- If at any point something doesn't match, break out and jump to the next sub-list
- If something matches, add it to that sublist
- Otherwise, create a list of its own
- Return the list of lists

- Since making the dictionary of each word is going to be the same,
I'll create a separate re-usable function for it

Implement:
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        # Output: [["act", "cat"],["stop", "pots", "tops"], ["hat"]]
        
        output = [] # [["act"], ["pots", "tops"]]

        for current_word in strs: # tops O(strs)

            added = False # boolean to represent if the word has been added or not

            for anagram_list in output: # ["pots"] O(strs)
                # We just need to compare with the first word
                first_word = anagram_list[0] # pots

                is_anagram = self.checkAnagram(current_word, first_word) # true
                if is_anagram:
                    anagram_list.append(current_word)
                    added = True
                    break
            
            if not added:
                output.append([current_word])
        
        return output

    def createDictionary(self, string: str) -> dict: # pots # O(longest string)
        return_dict = {} # {t : 1, o : 1, p : 1, s : 1}
        for letter in string: # s # O (longest string)
            if letter in return_dict: # false O(1)
                return_dict[letter] += 1
            else:
                return_dict[letter] = 1

        return return_dict

    def checkAnagram(self, word_1: str, word_2: str) -> bool: # O(longest string)
        # dict_1 = {t : 1, o : 1, p : 1, s : 1}
        # dict_2 = {p : 1, o : 1, t : 1, s : 1}

        if len(word_1) != len(word_2):
            return False

        dict_1 = self.createDictionary(word_1)
        dict_2 = self.createDictionary(word_2)
        
        for key, value in dict_1.items(): # s, 1 O(longest string)
            if key not in dict_2: # false O(1)
                return False
            
            if dict_2[key] != value: # O(1)
                return False

        return True

"""
Review:
- Done in comments

Evaluate:
- 
"""
        