"""

783. Minimum Distance Between BST Nodes : https://leetcode.com/problems/minimum-distance-between-bst-nodes/

BST가 주어졌을 때, 두 노드 사이의 minimum difference를 구하는 문제
- BST의 노드의 개수는 2개 이상 100개 이하이다
- BST는 항상 valid하며, 각 노드의 값은 정수이고, 모든 노드의 값은 다르다

Example:
- Input : [4,2,6,1,3,null,null]
- Output : 1
- 1과 2, 2와 3, 3과 4의 difference가 1

Note:
트리를 순회하여 값들을 전부 list에 저장한 후, 정렬하여 구하는 방식
문제 530번과 동일

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes, diff = [], sys.maxsize
        def solve(self, node: TreeNode):
            nodes.append(node.val)
            if node.left:
                solve(self, node.left)
            if node.right:
                solve(self, node.right)
        solve(self, root)
        nodes = sorted(nodes)
        for i in range(len(nodes)-1):
            if nodes[i+1]-nodes[i] < diff:
                diff = nodes[i+1]-nodes[i]
            if diff == 1:
                return diff
        return diff