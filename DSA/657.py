

from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        counter_var = Counter(moves)
        return counter_var['U'] == counter_var['D'] and counter_var['L'] == counter_var['R']
