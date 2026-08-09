# 530. Minimum Absolute Difference in BST
# Note: This question is the same as 
# 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minimum = float('inf')

        def inorder(node):
            if not node:
                return

            # Left
            inorder(node.left)

            # Process current node
            if self.prev is not None:
                self.minimum = min(self.minimum, node.val - self.prev)

            self.prev = node.val

            # Right
            inorder(node.right)

        inorder(root)
        return self.minimum


# -------------------------
# Helper function to build tree from list
# -------------------------
def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i in range(len(values)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(values):
                nodes[i].left = nodes[left_index]
            if right_index < len(values):
                nodes[i].right = nodes[right_index]

    return nodes[0]


# -------------------------
# Main execution
# -------------------------
if __name__ == "__main__":
    # Example 1: [4,2,6,1,3]
    values = [4, 2, 6, 1, 3]
    root = build_tree(values)

    sol = Solution()
    result = sol.getMinimumDifference(root)

    print("Minimum Absolute Difference:", result)