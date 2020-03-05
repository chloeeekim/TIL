"""

124. Binary Tree Maximum Path Sum : https://leetcode.com/problems/binary-tree-maximum-path-sum/

binary tree가 하나 주어졌을 때, 각 노드의 값들의 합이 최대가 되는 path의 합을 구하는 문제
- path는 적어도 하나의 노드가 포함되어야 하며, root 노드를 지날 필요는 없다

Example:
- Input : [1,2,3]
- Output : 6

- Input : [-10,9,20,null,null,15,7]
- Output : 42

Note:
solve() 함수를 생성하여 recursive하게 해결
각 노드를 순회하며 왼쪽 서브트리에서의 최대합과 오른쪽 서브트리에서의 최대합을 확인
해당 노드에서 부모 노드로 연결될 수 없는 path(왼쪽-자신-오른쪽의 구조로 된 path)의 경우에는 maxSum과 비교
부모 노드로 연결될 수 있는 path(왼쪽-자신, 자신-오른쪽의 구조로 된 path)의 경우에는 해당 노드의 값을 더한 후 부모 노드로 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = root.val
        def solve(self, node: TreeNode) -> int:
            left, right = 0, 0
            if node.left :
                left = max(solve(self, node.left), left)
            if node.right :
                right = max(solve(self, node.right), right)
            self.maxSum = max(self.maxSum, node.val + left + right)
            return node.val + left if left > right else node.val + right
        solve(self, root)
        return self.maxSum