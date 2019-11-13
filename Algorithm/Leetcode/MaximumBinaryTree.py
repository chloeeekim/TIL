"""

654. Maximum Binary Tree : https://leetcode.com/problems/maximum-binary-tree/

정수로 이루어진 list가 주어졌을 때, 해당 리스트를 maximum binary tree로 변환하는 문제
- root는 list의 가장 큰 값이 된다
- left subtree는 가장 큰 값을 기준으로 나뉘어진 왼쪽 sublist를 maximum tree로 만든 것이다
- right subtree는 가장 큰 값을 기준으로 나뉘어진 오른쪽 sublist를 maximum tree로 만든 것이다
- 입력 list의 사이즈는 [1,1000] 범위이다

Example:
- Input : [3,2,1,6,0,5]
- Output : [6,3,5,null,2,0,null,null,1]

Note:
construct() 함수를 생성하여 recursive하게 해결
sublist의 시작과 끝 인덱스를 가지고 subtree 생성

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        res = TreeNode(-1)
        def construct(self, parent: TreeNode, start: int, end: int, isLeft: bool) :
            if start == end :
                return
            temp = nums[start:end]
            maxnum = max(temp)
            maxidx = temp.index(maxnum)
            node = TreeNode(maxnum)
            if isLeft:
                parent.left = node
            else :
                parent.right = node
            if start != maxidx + start :
                construct(self, node, start, maxidx + start, True)
            if end != start + maxidx + 1 :
                construct(self, node, start + maxidx + 1, end, False)
        construct(self, res, 0, len(nums), True)
        return res.left