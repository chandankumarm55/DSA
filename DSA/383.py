'''
frist we initailize the empty dict magazine_counts = {}
next we count the each appearence and store it in magazine_counts 
next we check the if the charcter of ransomNote not in magazine_counts and we find the match of count by using magazine_counts[char] == 0: 
if the abve condition is true we return False 
and other wise will retrun true if we can make ransomNote from magazine_counts
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Count occurrences of each character in magazine
        magazine_counts = {}
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if char not in magazine_counts or magazine_counts[char] == 0:
                return False
            magazine_counts[char] -= 1
        
        return True

