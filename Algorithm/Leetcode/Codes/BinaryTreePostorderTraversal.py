"""

145. Binary Tree Postorder Traversal : https://leetcode.com/problems/binary-tree-postorder-traversal/

binary tree가 하나 주어졌을 때, 해당 트리의 postorder traversal의 결과를 구하는 문제

Example:
- Input : [1,null,2,3]
- Output : [3,2,1]

Note:
postorder() 함수를 만들어 recursive하게 해결
inorder와 함수 호출 순서만 변경

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(self, node: TreeNode) -> None:
            if not node :
                return          
            postorder(self, node.left)
            postorder(self, node.right)
            res.append(node.val)
        postorder(self, root)
        return res