'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]'''




class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}
        for word in strs:
            sorted_word =''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word]=[]
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
        