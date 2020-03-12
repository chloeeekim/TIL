"""

563. Binary Tree Tilt : https://leetcode.com/problems/binary-tree-tilt/

binary tree가 하나 주어졌을 때, 해당 트리 전체의 tilt를 구하는 문제
- 특정 노드의 tilt 값은 왼쪽 서브트리와 오른쪽 서브트리 각각의 합의 absolute difference이다
- Null 노드의 tilt는 0이다
- 전체 트리의 tilt는 모든 노드의 tilt 값의 합이다

Example:
- Input : [1,2,3]
- Output : 1
- 0 (node 2) + 0 (node 3) + 1 (node 1) = 1

Note:
solve() 함수를 생성하여 recursive하게 해결
각 노드를 순회하며 왼쪽 서브트리의 합과 오른쪽 서브트리의 합을 확인
해당 노드의 tilt 값을 구하여 total에 더하고, 자신의 값을 더하여 부모 노드로 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root :
            return 0
        self.total = 0
        def solve(self, node: TreeNode) -> int :
            left, right = 0, 0
            if node.left :
                left = solve(self, node.left)
            if node.right :
                right = solve(self, node.right)
            tilt = abs(left - right)
            self.total += tilt
            return left + right + node.val
        solve(self, root)
        return self.total