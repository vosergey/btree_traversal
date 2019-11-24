import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def iterativelyLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque()
        
        queue.append(root)
        
        level = 0
        result = []
        
        while queue:
            
            result.append([node.val for node in queue])
            
            queue_len = len(queue)
            
            i = 0
            
            while i < queue_len:
                
                current = queue.popleft()
                
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)
                    
                i += 1
                    
            level += 1
            
        return result