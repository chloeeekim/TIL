"""

105. Construct Binary Tree from Preorder and Inorder Traversal : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

어떤 트리의 inorder, preorder traversal 결과가 리스트로 주어졌을 때, 트리를 복원하는 문제
- 트리 내에 중복된 값은 없다고 가정한다

Example:
- Input : preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
- Output : [3,9,20,null,null,15,7]

Note:
recursive하게 해결
preorder 리스트의 첫 번째 값은 무조건 root가 되고, inorder 리스트에서 root 값을 기준으로 left children과 right children으로 구분된다
위 조건이 모든 subtree에 대해서도 만족

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            rootval = preorder.pop(0)
            root = TreeNode(rootval)
            idx = inorder.index(rootval)
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root