"""

102. Binary Tree Level Order Traversal : https://leetcode.com/problems/binary-tree-level-order-traversal/

binary tree가 하나 주어졌을 때, 해당 트리의 level order traversal의 결과를 구하는 문제
- 왼쪽에서 오른쪽 순서로 순회하며, 레벨별로 나타내어야 한다

Example:
- Input : [3,9,20,null,null,15,7]
- Output : [[3],[9,20],[15,7]]

Note:
stack을 사용하여 해결
해당 노드의 레벨을 확인하기 위하여 stack에서 [node, level]의 형태로 관리

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        res = [[]]
        stack = [[root, 0]]
        while stack :
            temp = stack.pop()
            node, level = temp[0], temp[1]
            if len(res) <= level :
                res.append([node.val])
            else :
                res[level].append(node.val)
            if node.right :
                stack.append([node.right, level + 1])
            if node.left :
                stack.append([node.left, level + 1])
        return res      