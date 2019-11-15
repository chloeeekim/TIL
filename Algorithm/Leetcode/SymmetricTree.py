"""

101. Symmetric Tree : https://leetcode.com/problems/symmetric-tree/

binary tree가 하나 주어졌을 때, 해당 트리가 symmetric인지 확인하는 문제

Example:
- Input : [1,2,2,3,4,4,3]
- Output : true

- Input : [1,2,2,null,3,null,3]
- Output : false

Note:
solve() 함수를 생성하여 recursive하게 해결
각 노드의 대칭되는 노드를 비교하여 값이 다르거나 한 쪽 노드가 존재하지 않는 경우 False를 리턴

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root :
            return True
        def solve(self, node1: TreeNode, node2: TreeNode) -> bool :
            if not node1 and not node2 :
                return True
            elif (not node1 and node2) or (node1 and not node2) :
                return False
            if node1.val != node2.val :
                return False
            return solve(self, node1.left, node2.right) and solve(self, node1.right, node2.left)
        return solve(self, root.left, root.right)