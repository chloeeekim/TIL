"""

199. Binary Tree Right Side View : https://leetcode.com/problems/binary-tree-right-side-view/

binary tree가 하나 주어졌을 때, 해당 트리를 오른쪽에서 본 결과를 구하는 문제
- 결과는 top에서 bottom 순서

Example:
- Input : [1,2,3,null,5,null,4]
- Output : [1,3,4]

Note:
- Solution 1
getview() 함수를 만들어서 recursive하게 해결
왼쪽에서부터 depth first search로 트리를 순회하며 view 리스트를 갱신
- Solution 2
queue를 사용하여 해결
각 레벨별로 tqueue 리스트를 두어 한 레벨이 끝날 때마다 queue와 결과 리스트를 갱신하는 방식
가장 마지막에 방문한 node가 right side view에 해당하므로, 마지막 노드를 결과 리스트에 append

"""

# Solution 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        view = []
        def getview(self, node: TreeNode, depth: int) :
            if len(view) < depth :
                view.append(node.val)
            else :
                view[depth-1] = node.val
            if node.left :
                getview(self, node.left, depth+1)
            if node.right :
                getview(self, node.right, depth+1)
        getview(self, root, 1)
        return view

# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        view = []
        queue, tqueue = [root], []
        while queue:
            node = queue.pop(0)
            if node.left:
                tqueue.append(node.left)
            if node.right:
                tqueue.append(node.right)
            if not queue:
                view.append(node.val)
                queue, tqueue = tqueue, []
        return view