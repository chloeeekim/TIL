"""

543. Diameter of Binary Tree : https://leetcode.com/problems/diameter-of-binary-tree/

binary tree가 하나 주어졌을 때, 가장 긴 path의 길이를 구하는 문제
- path의 길이는 두 노드 사이의 거리이며, root 노드를 지날 필요는 없다

Example:
- Input : [1,2,3,4,5]
- Output : 3
- [4,2,1,3] 혹은 [5,2,1,3]이 가장 긴 path

Note:
solve() 함수를 생성하여 recursive하게 해결
각 노드를 순회하며 왼쪽 서브트리에서의 최대 길이와 오른쪽 서브트리에서의 최대 길이를 확인
해당 노드에서 부모 노드로 연결될 수 없는 path(왼쪽-자신-오른쪽의 구조로 된 path)의 경우에는 maxlen과 비교
부모 노드로 연결될 수 있는 path(왼쪽-자신, 자신-오른쪽의 구조로 된 path)의 경우에는 위 노드까지의 거리인 1을 더한 후 부모 노드로 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root :
            return 0
        self.maxlen = 0
        def solve(self, node: TreeNode) -> int :
            left, right = 0, 0
            if node.left :
                left = solve(self, node.left)
            if node.right :
                right = solve(self, node.right)
            self.maxlen = max(self.maxlen, left + right)
            return left + 1 if left > right else right + 1
        solve(self, root)
        return self.maxlen