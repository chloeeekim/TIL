"""

404. Sum of Left Leaves : https://leetcode.com/problems/sum-of-left-leaves/

binary tree가 주어졌을 때, 모든 left leaves의 합을 구하는 문제

Example:
- Input : [3,9,20,null,null,15,7]
- Output : 24
- left leaf는 9와 15 두 개

Note:
solve() 함수를 생성하여 recursive하게 해결
left leaf인지 판별하기 위하여 함수 호출 시에 bool 타입의 isLeft를 넘겨주는 방식으로 구현

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root :
            return 0
        def solve(self, node: TreeNode, isLeft: bool) -> int :
            if not node.left and not node.right :
                if isLeft :
                    return node.val
                else :
                    return 0
            res = 0
            if node.left :
                res += solve(self, node.left, True)
            if node.right :
                res += solve(self, node.right, False)
            return res
        return solve(self, root, False)