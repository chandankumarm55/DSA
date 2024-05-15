class Solution:
    def isValid(self, s):
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in brackets_map.keys():  # If it's a closing bracket
                if not stack or stack[-1] != brackets_map[char]:
                    return False
               4 stack.pop()
            else:  # If it's neither an opening nor a closing bracket
                return False
        
        # If the stack is empty, it means all brackets are matched
        return not stack

