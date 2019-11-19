"""

230. Kth Smallest Element in a BST : https://leetcode.com/problems/kth-smallest-element-in-a-bst/

binary search tree가 주어졌을 때, K번째로 작은 노드의 값을 구하는 문제
- k는 항상 valid하다고 가정한다 (1 <= k <= BST의 전체 노드 수)

Example:
- Input : [3,1,4,null,2], k = 1
- Output : 1

- Input : [5,3,6,2,4,null,null,1], k = 3
- Output : 3

Note:
solve() 함수를 생성하여 recursive하게 해결
bst를 값이 작은 순서대로 순회하면서 bst 리스트에 append하여 k번째 작은 노드의 값을 구하는 방식
참고) 굉장히 단순한 방식이라 시간이 오래 걸릴 것이라 예상했으나 99.57%가 나와서 당황

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        bst = []
        def solve(self, node: TreeNode) :
            if len(bst) >= k :
                return
            if node.left :
                solve(self, node.left)
            bst.append(node.val)
            if node.right :
                solve(self, node.right)
        solve(self, root)
        return bst[k-1]