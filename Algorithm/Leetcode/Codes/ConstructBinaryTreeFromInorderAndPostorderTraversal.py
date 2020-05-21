"""

106. Construct Binary Tree from Inorder and Postorder Traversal : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

어떤 트리의 inorder, postorder traversal 결과가 리스트로 주어졌을 때, 트리를 복원하는 문제
- 트리 내에 중복된 값은 없다고 가정한다

Example:
- Input : inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
- Output : [3,9,20,null,null,15,7]

Note:
recursive하게 해결
inorder와 preorder로 트리를 복원하는 문제에서 약간만 변형
postorder 리스트의 마지막 값이 root가 되고, inorder 리스트에서 root 값을 기준으로 left children과 right children으로 구분된다
위 조건이 모든 subtree에 대해서도 만족
preorder에서는 left children을 먼저 구하고, right children을 구하는 순서였으나,
postorder에서는 반대로 right children을 먼저 구하고, left children을 구하는 순서

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            rootval = postorder.pop(-1)
            root = TreeNode(rootval)
            idx = inorder.index(rootval)
            root.right = self.buildTree(inorder[idx+1:], postorder)            
            root.left = self.buildTree(inorder[:idx], postorder)
            return root