'''
Problem: we have to find the hammingWeight in the given number of binary representation
Solution: so two solve this problem we need to follow simple three steps to solve the problem 
mannul calculation of binaryrepresentation is :
def convertingBinary(num):
            currentBinary=''
            while num>0:
                rem = num%2
                currentBinary+=str(rem)
                num=num//2
            return currentBinary
            
1: frist we neeed to convert the decimal representation to  binary represetation to find the number of 1's in the binary code
2: next we need to count the number of once in the binaryrepresentation so inorder to find the we used inbuilt function count
to count it. we can also use mannul calculation using for loop 
3: next and last step is to return the count 

Time Complexity is = O(log n)
Space Complexity is =O(1)
'''
class Solution(object):
    def hammingWeight(self, n):
        binaryRepresention = bin(n).replace('0b','')
        count = binaryRepresention.count('1')
        return count
