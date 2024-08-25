'''
Example :
Input: root = [1,null,2,3]
Output: [3,2,1]

Problem:
problem is to do the post order Traversal of the given tree 
what is postOrder:
frist visting the left part of the root node and then traversing the right part of the root node and finally traversing the 
root node of the given tree . generally it followes below direction ;

LEFT SUBTREE ---> RIGHT SUBTREE ----> ROOT NODE

Solution :
 how we can achieve this , answer is we achieve this using recurssion easly , so we traverse the left of the tree and then right 
 child of the node :
 then finally returning the result array which holds the post order element of the given tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result =[]
        def traversal(node):
            if node is None:
                return 
            traversal(node.left)
            traversal(node.right)
            result.append(node.val)
        traversal(root)
        return result
        
        
