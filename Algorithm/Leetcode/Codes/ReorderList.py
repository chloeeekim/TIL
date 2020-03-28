"""

143. Reorder List : https://leetcode.com/problems/reorder-list/

linked list가 하나 주어졌을 때, 노드의 순서를 바꾸는 문제
- L0 -> L1 -> L2 -> ... -> Ln 의 노드를 L0 -> Ln -> L1 -> Ln-1 -> L2 -> ... 로 변경
- 각 노드의 값을 바꾸는 것이 아니라 노드 자체를 변경할 것

Example:
- Input : 1->2->3->4
- Output : 1-->4->2->3

- Input : 1->2->3->4->5
- Output : 1->5->2->4->3

Note:
처음 linked list를 순회하며 노드 정보를 list에 저장
이후 left, right의 값을 변경하며 노드의 연결 정보를 변경
cycle이 생기지 않도록 마지막 노드의 next를 None으로 설정

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head :
            return head
        nodes, node = [], head
        while node :
            nodes.append(node)
            node = node.next
        left, right = 0, len(nodes) - 1
        while left < right :
            nodes[left].next = nodes[right]
            nodes[right].next = nodes[left + 1]
            left += 1
            right -= 1
        nodes[left].next = None