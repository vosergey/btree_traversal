import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
      

def iterativelyPostorderTraversal(self, root: TreeNode) -> List[int]:
        
     if not root:
            return []
        
        result, stack = [], []
        
        stack.append(root)
        
        while len(stack) > 0:
            
            root = stack[-1]
            
            if root.left or root.right:
              
                if root.right:
                    stack.append(root.right)
                    root.right = None
                
                if root.left:
                    stack.append(root.left)
                    root.left = None
            else:
                
                result.append(stack.pop().val)
        return result
    
def recursivelyPostorderTraversal(root: TreeNode):
        
    if type(root) is not TreeNode:
        return None
            
    result = []
        
    if not root.left ==  None:
        result += self.recursivelyPostorderTraversal(root.left)

    if not root.right == None:
         
        result += self.recursivelyPostorderTraversal(root.right)
        
    result.append(root.val)

    return result