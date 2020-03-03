"""

513. Find Bottom Left Tree Value : https://leetcode.com/problems/find-bottom-left-tree-value/

binary tree가 주어졌을 때, 가장 아래쪽의 row에서 가장 왼쪽에 위치한 노드의 값을 찾는 문제

Example:
- Input : [2,1,3]
- Output : 1

- Input : [1,2,3,4,null,5,6,null,null,7]
- Output : 7

Note:
solve() 함수를 생성하여 recursive하게 해결
각 레벨에서 가장 왼쪽에 있는 노드를 우선적으로 방문하도록 구현
트리의 탐색이 종료되면 rows 리스트에는 각 레벨의 가장 왼쪽에 있는 노드의 값이 저장

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        rows = []
        def solve(self, node: TreeNode, level: int) :
            if len(rows) <= level :
                rows.append(node.val)
            if node.left :
                solve(self, node.left, level + 1)
            if node.right :
                solve(self, node.right, level + 1)
        solve(self, root, 0)
        return rows[-1]