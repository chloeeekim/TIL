"""

725. Split Linked List in Parts : https://leetcode.com/problems/split-linked-list-in-parts/

linked list가 주어졌을 때, k개의 part로 나누는 문제
- 각각의 part는 가능한 같은 길이의 linked list가 되어야 한다
- 모든 두 part의 길이의 차이가 1을 넘어서는 안 된다
- 몇몇 part는 None이 될 수 있다
- part는 주어진 linked list의 순서대로 나누어져야 한다
- size가 큰 part가 size가 작은 part보다 먼저 나와야 한다

Example:
- Input : root = [1, 2, 3], k = 5
- Output : [[1],[2],[3],[],[]]
- []는 None을 나타낸 것

- Input : root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
- Output : [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

Note:
linked list를 우선 순회하여 노드 정보를 전부 list에 저장
주어진 linked list의 길이와 k의 div, mod를 구하여 각 part에 들어가야 하는 linked list의 길이를 구하여 해결
nodes를 매번 사용한 노드를 제외한 리스트로 갱신하였으나, i에 대한 인덱스로 계산하면 갱신할 필요는 없음

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        nodes, node = [], root
        while node:
            nodes.append(node)
            node = node.next
        div, mod = divmod(len(nodes), k)
        res = []
        for i in range(k):
            if not nodes:
                res.append(None)
                continue
            if mod > 0:
                nodes[div].next = None
            else:
                nodes[div-1].next = None
            res.append(nodes[0])
            nodes = nodes[div+1:] if mod > 0 else nodes[div:]
            mod -= 1
        return res