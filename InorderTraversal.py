import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
def iterativelyInorderTraversal(root: TreeNode):
    traversal = []

    stack = collections.deque()
        
    current = root
        
    while current or stack:
    
        while current:
            stack.append(current)
            current = current.left
                
        current = stack.pop()
        traversal.append(current.val)
        
        current = current.right
            
    return traversal

        
def recursivelyInorderTraversal(root: TreeNode):
    if type(root) is not TreeNode:
        return None
            
    result = []
        
    if not root.left ==  None:
        result += self.inorderTraversal(root.left)
            
    result.append(root.val)
        
    if not root.right == None:
         result += self.inorderTraversal(root.right)

    return result