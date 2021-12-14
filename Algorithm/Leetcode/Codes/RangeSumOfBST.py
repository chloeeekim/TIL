"""

938. Range Sum of BST : https://leetcode.com/problems/range-sum-of-bst/

BST와 범위가 주어졌을 때, 해당 범위 안에 포함되는 노드들의 합을 구하는 문제
- 범위 low와 high까지 포함한다
- 모든 노드의 값은 unique하다

Example:
- Input : root = [10,5,15,3,7,null,18], low = 7, high = 15
- Output : 32
- 7 + 10 + 15 = 32

- Input : root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
- Output : 23
- 6 + 7 + 10 = 23

Note:
recursive하게 트리를 탐색
범위를 벗어나는 경우 방문할 필요가 없으므로 제외

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        res = root.val if root.val >= low and root.val <= high else 0
        if root.val > low:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            res += self.rangeSumBST(root.right, low, high)
        return res