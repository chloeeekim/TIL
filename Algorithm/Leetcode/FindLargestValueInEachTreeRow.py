"""

515. Find Largest Value in Each Tree Row : https://leetcode.com/problems/find-largest-value-in-each-tree-row/

binary tree가 주어졌을 때, 각 row의 가장 큰 값들을 찾는 문제

Example:
- Input : [1,3,2,5,3,null,9]
- Output : [1,3,9]

Note:
solve() 함수를 생성하여 recursive하게 해결
각 노드가 몇 번째 row인지 확인하기 위하여 level 값을 포함하여 호출

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root :
            return []
        res = []
        def solve(self, node: TreeNode, level: int) :
            if len(res) > level :
                res[level] = max(node.val, res[level])
            else :
                res.append(node.val)
            if node.left :
                solve(self, node.left, level + 1)
            if node.right :
                solve(self, node.right, level + 1)
        solve(self, root, 0)
        return res