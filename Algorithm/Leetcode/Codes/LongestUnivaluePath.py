"""

687. Longest Univalue Path : https://leetcode.com/problems/longest-univalue-path/

binary tree가 주어졌을 때, 같은 값으로 이루어진 node들을 연결하는 path의 최대 길이를 구하는 문제
- path는 root를 지나지 않을 수도 있다
- 두 노드 사이의 path의 길이는 path에 포함된 edge의 개수이다
- 주어진 트리의 노드 개수는 10000개를 넘지 않으며, 트리의 높이는 1000을 넘지 않는다

Example:
- Input : [5,4,5,1,1,null,5]
- Output : 2

- Input : [1,4,5,4,4,null,5]
- Output : 2

Note:
solve() 함수를 생성하여 recursive하게 해결
특정 노드에서 만들어지는 path의 경우의 수는 총 3가지
left/right children에서 이어서 부모 노드로 이어지는 경우와 자신을 포함한 left/right children 양쪽으로 이어지는 경우
최대값을 갱신한 후, 부모 노드로 left 혹은 right 중 큰 값을 return

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def solve(node: TreeNode) -> int:
            left = right = 0
            if node.left:
                left = solve(node.left)+1
                left = left if node.val == node.left.val else 0
            if node.right:
                right = solve(node.right)+1
                right = right if node.val == node.right.val else 0
            tmp = max(left+right, left, right)
            self.res = max(self.res, tmp)
            return max(left, right)
        if not root:
            return 0
        self.res = 0
        solve(root)
        return self.res