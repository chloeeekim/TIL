"""

144. Binary Tree Preorder Traversal : https://leetcode.com/problems/binary-tree-preorder-traversal/

binary tree가 하나 주어졌을 때, 해당 트리의 preorder traversal의 결과를 구하는 문제

Example:
- Input : [1,null,2,3]
- Output : [1,2,3]

Note:
preorder() 함수를 만들어 recursive하게 해결
inorder와 함수 호출 순서만 변경

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preorder(self, node: TreeNode) -> None:
            if not node :
                return            
            res.append(node.val)
            preorder(self, node.left)
            preorder(self, node.right)
        preorder(self, root)
        return res