from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        # Count the occurrences of characters in t
        target_count = Counter(t)
        required_chars = len(target_count)

        # Use two pointers to define the window
        left, right = 0, 0
        formed_chars = 0
        window_count = {}
        min_length = float('inf')
        min_window = ""

        while right < len(s):
            # Expand the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            if char in target_count and window_count[char] == target_count[char]:
                formed_chars += 1

        
            while formed_chars == required_chars and left <= right:
                char = s[left]
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed_chars -= 1

                left += 1

            right += 1

        return min_window

# Test cases
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC")) 
print(solution.minWindow("a", "a"))                # Output: "a"
print(solution.minWindow("a", "aa"))               # Output: ""
