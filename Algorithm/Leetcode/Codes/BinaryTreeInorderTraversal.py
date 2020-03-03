"""

94. Binary Tree Inorder Traversal : https://leetcode.com/problems/binary-tree-inorder-traversal/

binary tree가 하나 주어졌을 때, 해당 트리의 inorder traversal의 결과를 구하는 문제

Example:
- Input : [1,null,2,3]
- Output : [1,3,2]

Note:
inorder() 함수를 만들어 recursive하게 해결

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(self, node: TreeNode) -> None:
            if not node :
                return
            inorder(self, node.left)
            res.append(node.val)
            inorder(self, node.right)
        inorder(self, root)
        return res