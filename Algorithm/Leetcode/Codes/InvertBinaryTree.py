"""

226. Invert Binary Tree : https://leetcode.com/problems/invert-binary-tree/

binary tree가 주어졌을 때, 이를 좌우로 뒤집는 문제

Example:
- Input : [4,2,7,1,3,6,9]
- Output : [4,7,2,9,6,3,1]

Note:
invert() 함수를 만들어서 해당 노드의 자식 노드 두 개를 바꿔주는 방식으로 구현
참고) root가 비어 있는 경우([])도 있음

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root :
            return root
        def invert(self, node: TreeNode):
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.right :
                invert(self, node.right)
            if node.left :
                invert(self, node.left)
        invert(self, root)
        return root