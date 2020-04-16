"""

508. Most Frequent Subtree Sum : https://leetcode.com/problems/most-frequent-subtree-sum/

트리가 주어졌을 때, most frequent subtree sum을 찾는 문제
- subtree sum이란 subtree에 포함되는 모든 노드의 value의 합
- most frequent subtree sum이 여러 개인 경우, 순서에 상관없이 모든 값을 리턴한다

Example:
- Input : [5,2,-3]
- Output : [2,-3,4]
- 결과는 순서가 상관 없으므로 [-3,4,2] 등 여러 가지 답이 가능하다

- Input : [5,2,-5]
- Output : [2]
- subtree sum이 2인 경우는 2가지가 있고, -5인 경우는 1가지

Note:
solve() 함수를 생성하여 recursive하게 해결
dict를 사용하여 각 subtree sum의 가짓수를 저장
트리를 전부 순회한 후, subtree sum의 등장 횟수별로 정렬하여 결과 list를 생성한다

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sums = {}
        def solve(self, node: TreeNode) -> int:
            s = node.val
            if node.left:
                s += solve(self, node.left)
            if node.right:
                s += solve(self, node.right)
            sums[s] = 1 if s not in sums else sums[s]+1
            return s
        solve(self, root)
        sums = sorted(sums.items(), key=(lambda x: x[1]), reverse=True)
        m, res = sums[0][1], []
        for s in sums:
            if s[1] != m:
                break
            res.append(s[0])
        return res