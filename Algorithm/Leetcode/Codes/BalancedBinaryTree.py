"""

110. Balanced Binary Tree : https://leetcode.com/problems/balanced-binary-tree/

binary tree가 하나 주어졌을 때, 해당 트리가 height-balanced tree인지 확인하는 문제
- height-balanced BST란 각 서브트리의 높이 차이가 1보다 크지 않은 경우이다

Example:
- Input : [3,9,20,null,null,15,7]
- Output : true

- Input : [1,2,2,3,3,null,null,4,4]
- Output : false

Note:
solve() 함수를 만들어 recursive하게 해결
각 subtree들의 높이를 구하여 높이를 비교
subtree의 높이의 차가 1보다 큰 경우(balanced tree가 아닌 경우) -1을 리턴

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def solve(self, node: TreeNode) -> int :
            if not node :
                return 0
            left, right = 0, 0
            if node.left :
                left = solve(self, node.left)
                if left == -1 :
                    return -1
            if node.right :
                right = solve(self, node.right)
                if right == -1 :
                    return -1
            if abs(left-right) > 1 :
                return -1
            return max(left, right) + 1
        return True if solve(self, root) != -1 else False