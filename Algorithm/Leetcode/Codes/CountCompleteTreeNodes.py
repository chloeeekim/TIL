"""

222. Count Complete Tree Nodes : https://leetcode.com/problems/count-complete-tree-nodes/

complete binary tree가 주어졌을 때, 전체 노드의 개수를 구하는 문제
- O(n) time complexity 이하로 디자인할 것
- 주어진 tree는 complete하다는 것이 보장된다

Example:
- Input : root = [1,2,3,4,5,6]
- Output : 6

- Input : root = []
- Output : 0

- Input : root = [1]
- Output : 1

Note:
recursive하게 해결
complete한 것을 고려하지 않았으므로 다른 방식으로 최적화해 볼 것

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        if root.left:
            count += self.countNodes(root.left)
        if root.right:
            count += self.countNodes(root.right)
        return count