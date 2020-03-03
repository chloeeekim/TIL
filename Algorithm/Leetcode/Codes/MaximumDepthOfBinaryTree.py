"""

104. Maximum Depth of Binary Tree : https://leetcode.com/problems/maximum-depth-of-binary-tree/

binary tree가 주어졌을 때, 해당 트리의 최대 depth를 구하는 문제
- depth는 root 노드에서부터 leaf 노드까지의 길이를 의미한다
- leaf 노드는 자식 노드가 없는 노드이다

Example:
- Input : [3,9,20,null,null,15,7]
- Output : 3

Note:
stack을 사용하여 depth first search 방식으로 트리 탐색

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        stack = [[root, 1]]
        res = 0
        while stack :
            temp = stack.pop()
            node = temp[0]
            if not node.right and not node.left :
                res = max(res, temp[1])
            if node.right :
                stack.append([node.right, temp[1] + 1])
            if node.left :
                stack.append([node.left, temp[1] + 1])
        return res