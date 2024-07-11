'''
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

we can use the stack data structure to solve this type of problems , 
step 1 : initialize  stack = [] to keep track of the element added
step 2 : itertate over the elements in string s :
condtition - if the char is == ')' tha means we encounter the closing brackets and we have to reverse the latest added elements
till '(; brackets .

              if char ==')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(temp)
  we used a temporary varible to keep track about the atlest pop ellement till '(' encountered . 
  if the stack[-1] element is equal to '(' we will remove from the stack and add the reversed temp list to stack back using 
  stack.extend(temp)
  step 3 : if the current character is not ')' then we simply add the char into stack
  step 4 : we retrun the reversed char 
'''
class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        
        for char in s:
            if char ==')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(temp)
            else :
                stack.append(char)
        return ''.join(stack)
