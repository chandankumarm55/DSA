'''
Problem : 
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.


'''
class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_pairs(s, first, second, points):
            print(s)
            total=0
            stack=[]
            for char in s:
                if stack and stack[-1]==first and char==second:
                    total+=points
                    stack.pop()
                else :
                    stack.append(char)
            return ''.join(stack) , total
        if x>y:
            s , points1 = remove_pairs(s,'a','b',x)
            _, points2 = remove_pairs(s,'b','a',y)
        else :
            s , points1 = remove_pairs(s,'b','a',y)
            _ , points2 = remove_pairs(s,'a','b',x)
        return points1 + points2
