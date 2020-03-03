"""

112. Path Sum : https://leetcode.com/problems/path-sum/

binary tree와 정수 sum이 주어졌을 때,
root-to-leaf path의 합이 sum과 동일한 path가 존재하는지를 찾는 문제
- leaf 노드는 child가 존재하지 않는다 (left, right 모두 None)

Example:
- Input : [5,4,8,11,null,13,4,7,2,null,null,null,1], sum = 22
- Output : true
- 5->4->11->2 = 22

Note:
위에서부터 내려오면서 left와 right child의 val에 현재 노드의 val을 더한다
특정 노드에서 left, right가 모두 None인 경우 값을 sum과 비교
모든 노드를 다 확인했음에도 sum과 동일한 값이 없는 경우 False를 리턴
참고) 중간 노드의 값이 sum보다 커지면 아래 노드는 확인하지 않도록 구현하려 했으나
음수 값이 포함되는 테스트 케이스가 존재하여 해당 조건은 삭제

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root :
            return False
        queue = [root]
        while queue :
            node = queue.pop(0)
            if node.left is None and node.right is None :
                if node.val == sum :
                    return True
            if node.left is not None :
                node.left.val += node.val
                queue.append(node.left)
            if node.right is not None :
                node.right.val += node.val
                queue.append(node.right)
        return False