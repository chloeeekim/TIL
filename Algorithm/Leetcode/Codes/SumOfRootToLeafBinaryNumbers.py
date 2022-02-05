"""

1022. Sum of Root To Leaf Binary Numbers : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

각 노드가 0과 1로 이루어진 binary tree가 주어졌을 때, root부터 leaf까지 만들어지는 binary들의 합을 구하는 문제
- 결과는 int로 출력하며, 32-bit integer에 맞도록 구성되어 있다

Example:
- Input : root = [1,0,1,0,1,0,1]
- Output : 22
- (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

- Input : root = [0]
- Output : 0

Note:
recursive하게 해결
binary이므로 << 연산자를 사용하여 계산

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def solve(node, binary):
            binary = (binary << 1) + node.val
            temp = 0
            if node.left:
                temp += solve(node.left, binary)
            if node.right:
                temp += solve(node.right, binary)
            if not node.left and not node.right:
                temp = binary
            return temp
        return solve(root, 0)