# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        stack = [root]

        while stack:
            
            node = stack.pop()
            self.res.append(node.val)
            
            if node.right : stack.append(node.right)
            if node.left : stack.append(node.left)
            
        
        return self.res



            
        ## Using recursion
        # def preorder(node):
        #     if node is None:
        #         return
            
        #     self.res.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)

        #     return node
        
        # preorder(root)
        # return self.res