import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def iterativePreorderTraversal(root: TreeNode) -> list[int]:
    traversal_queue = collections.deque()

    if type(root) is TreeNode:
        traversal_queue.append(root)
    else:
        return []

    traversal = []

    while traversal_queue:

        current = traversal_queue.popleft()

        if type(current.right) is TreeNode:
            traversal_queue.appendleft(current.right)

        if type(current.left) is TreeNode:
            traversal_queue.appendleft(current.left)

        traversal.append(current.val)

    return traversal


def recursivelyPreorderTraversal(root: TreeNode):
    if type(root) is not TreeNode:
        return None

    result = [root.val]

    if type(root.left) is TreeNode:
        result += recursivelyPreorderTraversal(root.left)

    if type(root.right) is TreeNode:
        result += recursivelyPreorderTraversal(root.right)

    return result
