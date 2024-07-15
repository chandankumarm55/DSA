'''
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

step 1 : create node_dict to sotre the every element in the decriptions and also it will store the tree refrece ,
children set to store the children of the root node 
step2 : iterate over decriptions and if the parent_val and child val not in decriptions and create new dict element , key as 
parent_val or child_val and create new tree node as value
step 3 : if the isleft is 1 then we need to add the child node in left of the parent node and if not means we need to add the 
child node in right of the parentnode
step 4 : add the child_val to find the parent node in last 
atep 5 : again iterate over the description and if the parent_val not in children that means the is the root node of the binary 
tree and return the binary tree node 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        node_dict ={}
        children = set()
        for parent_val , child_val , isleft in descriptions:
            if parent_val not in node_dict:
                node_dict[parent_val] = TreeNode(parent_val)
            if child_val not in node_dict:
                node_dict[child_val] = TreeNode(child_val)
            parent_node=node_dict[parent_val]
            child_node=node_dict[child_val]
            if isleft ==1:
                parent_node.left = child_node
            else :
                parent_node.right = child_node
            children.add(child_val)

        for parent_node , _,_ in descriptions:
            if parent_node not in children:
                return node_dict[parent_node]
        return None
