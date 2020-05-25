"""

889. Construct Binary Tree from Preorder and Postorder Traversal : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

어떤 트리의 preorder, postorder traversal 결과가 리스트로 주어졌을 때, 트리를 복원하는 문제
- 트리 내에 중복된 값은 없다고 가정한다

Example:
- Input : pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
- Output : [3,9,20,null,null,15,7]

Note:
recursive하게 해결
preorder 리스트의 첫 번째 값은 무조건 left children의 root가 되고, postorder 리스트의 마지막 값은 무조건 right children의 root가 된다
preorder 리스트를 기준으로 postorder 리스트에서 root 값을 기준으로 left children과 right children 리스트를 구분

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if post:
            rootval = pre.pop(0)
            post.pop(-1)
            root = TreeNode(rootval)
            if post:
                leftroot = post.index(pre[0])
                root.left = self.constructFromPrePost(pre, post[:leftroot+1])
                root.right = self.constructFromPrePost(pre, post[leftroot+1:])
            return root