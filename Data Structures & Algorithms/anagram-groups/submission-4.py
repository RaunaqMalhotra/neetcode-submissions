'''
Understand:
- Given a list of strings
- Group all strings which are anagrams of each other
- Return those groups as a list of lists

Anagram: All strings which have the same length, same characters, same frequence of characters but order of characters are different
    racecar and carrace

- To check for anagrams, we have to keep track of characters and its frequencies
- Dictionary:
    - key: character
    - value: frequency

Questions:
- What if the list is empty? Cannot be empty but string can be "" so Return [[""]]
- Take care of cases, a == A? Yes (I'll make everything lowercase)
- Return the output in any order

Match:
- Array/List
- Dictionaries

Plan:
Brute Force:
- 2 dictionaries
    - one for anagram characters
    - other for to store a word's anagrams
        - act: [cat]
        - pots: [tops, stop]
- Loop through every string at index i
- Nested loop for every string after that starting at i+1
- Checking if they're anagrams, putting them in a list corresponding to that dictionary
- O(n^2 * avg length of the strings) = O(n^2 * s)

More optimal:
- sort all the strings
    - sorted string = key
    - original string can be added to the list = value

For all strings, run merge sort (O(n) * s log s) where s is the average length of each string = O(n)

Implement:
'''

#strs = ["act","pots","tops","cat","stop","hat"]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dictionary = defaultdict(list)
        '''
        {
            act : [act, cat],
            opst : [pots, tops, stop]
            aht : [hat]
        }
        '''
        answer_list = [] # [[act, cat], [pots, tops, stop], [hat]]

        for string in strs: # cat
            sorted_string = "".join(sorted(string)) # act
            anagram_dictionary[sorted_string].append(string)

        for key, value in anagram_dictionary.items(): # 
            answer_list.append(value)

        return answer_list

'''
Review:
Done in comments

Evaluate:
- Time: O(n * s log s)
- Space: O(n) because the dictionary stores all the words in the original strs list
'''
        