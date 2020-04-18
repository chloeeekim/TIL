"""

530. Minimum Absolute Difference in BST : https://leetcode.com/problems/minimum-absolute-difference-in-bst/

BST가 주어졌을 때, 두 노드 사이의 minimum absolute difference를 구하는 문제
- BST에는 최소한 2개 이상의 노드가 존재한다
- BST는 non-negative values로 구성된다

Example:
- Input : [1,null,3,2]
- Output : 1
- 1과 2 혹은 2와 3의 absolute difference가 1

Note:
트리를 순회하여 값들을 전부 list에 저장한 후, 정렬하여 구하는 방식
문제 783번과 동일하다는 전제 하에, 530번에는 적혀 있지 않지만 노드의 값이 모두 다르다고 가정
따라서 absolute difference가 1이 되는 경우가 무조건 최저값이 된다

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
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