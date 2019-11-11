"""

637. Average of Levels in Binary Tree : https://leetcode.com/problems/average-of-levels-in-binary-tree/

비어 있지 않은 binary tree가 하나 주어졌을 때, 해당 트리의 각 level을 이루는 노드의 값의 평균을 구하는 문제

Example:
- Input : [3,9,20,15,7]
- Output : [3.00000,14.50000,11.00000]

Note:
solve() 함수를 생성하여 recursive하게 해결
rows 리스트에서 각 레벨별 노드 값의 합과 갯수를 관리
트리 순회가 끝나면 각 레벨 노드의 값의 평균을 구하여 리턴

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        rows = []
        def solve(self, node: TreeNode, level: int) :
            if len(rows) <= level :
                rows.append([node.val, 1])
            else :
                rows[level][0] += node.val
                rows[level][1] += 1
            if node.left :
                solve(self, node.left, level + 1)
            if node.right :
                solve(self, node.right, level + 1)
        solve(self, root, 0)
        res = []
        for row in rows :
            res.append(row[0] / row[1])
        return res