'''
TIME COMPLEXCITY IS O(n) and we have two helper funtion , one is to find the inorder travaseral of the given tree 
second one is for arranging the sorted val of tree and constructing the binary search tree by making the mid val as root element

'''
class Solution(object):
    def balanceBST(self, root):
        # performing inorder traversal to sort in to accesding order
        def Inorder(node):
            if not node:
                return []
            return Inorder(node.left)+[node.val] + Inorder(node.right)
        
        # constructing the binary seach tree by making the middle element 
        # as root node and arranging the left node of the root by [:mid]
        # and arranging the right node by [mid+1 :]
        def Construct(sorted_val):
            if not sorted_val :
                return None
            mid = len(sorted_val)//2
            root = TreeNode(sorted_val[mid])
            root.left = Construct(sorted_val[:mid])
            root.right = Construct(sorted_val[mid+1:])
            return root

        sorted_val = Inorder(root)
        return Construct(sorted_val)

