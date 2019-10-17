"""

114. Flatten Binary Tree to Linked List : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

binary tree가 주어졌을 때, 이를 flatten하는 문제
- 우측으로 편향되도록 바꾼다
- 순서는 depth-first
- in-place로 해결할 것

Example:
- Input : [1,2,5,3,4,null,6]
- Output : [1,null,2,null,3,null,4,null,5,null,6]

Note:
stack을 사용하여 depth-first로 노드 방문
참고) [None, None] 같은 형태의 테스트 케이스가 존재

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root :
            return
        stack = [root.right, root.left]
        root.left = root.right = None
        point = root
        while stack :
            node = stack.pop()
            if not node :
                continue
            if node.right is not None :
                stack.append(node.right)
                node.right = None
            if node.left is not None :
                stack.append(node.left)
                node.left = None
            point.right = node
            point = point.right
        return