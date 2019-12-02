"""

606. Construct String from Binary Tree : https://leetcode.com/problems/construct-string-from-binary-tree/

binary tree가 하나 주어졌을 때, 이를 preorder 순서로 순회한 결과를 parenthesis를 포함한 문자열로 변환하는 문제
- null node는 "()"로 나타내어진다
- empty parenthesis("()")의 존재유무가 트리를 나타내는 것과 상관없는 경우 표시를 생략한다

Example:
- Input : [1,2,3,4]
- Output : "1(2(4))(3)"
- "1(2(4)())(3()())"이 되어야 하나 나머지 empty parenthesis들은 의미가 없으므로 생략

- Input : [1,2,3,null,4]
- Output : "1(2()(4))(3)"
- 첫 empty parenthesis가 생략되면 다른 트리가 되어 버리므로 생략할 수 없다

Note:
solve() 함수를 생성하여 recursive하게 해결
preorder로 순회하는 방식으로 구성
자식 노드가 하나라도 있는 경우에는 무조건 왼쪽 자식 노드 위치에 parenthesis가 등장
오른쪽 자식 노드의 경우 존재하지 않으면 empty parenthesis 생략 가능

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = []
        def solve(self, node: TreeNode) :
            if not node :
                return
            res.append(str(node.val))
            if node.left or node.right :
                res.append('(')
                if node.left :
                    solve(self, node.left)
                res.append(')')
                if node.right :
                    res.append('(')
                    solve(self, node.right)
                    res.append(')')
        solve(self, t)
        return ''.join(res)