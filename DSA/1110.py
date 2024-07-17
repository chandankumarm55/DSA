'''
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Solution:
step1 :define a forest list to store the element and hashset for to_delete making sure that it has no duplicate 
step2 : next define a helper function to remove and iterate its left and right child to keep a track to add it forest list
   if current node is empty return node 
   if current node having right child means store it in node.left same for right node in node.right
   and append it to forest if it having 
   if the current node is not in delete set then directly return the current node as answer 
  step 3 : call the helper function recursively and if it returns the node then append to forest node 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        forest = []
        def helper(node):
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val in delete:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node
        root = helper(root)
        if root:
            forest.append(root)
        return forest
