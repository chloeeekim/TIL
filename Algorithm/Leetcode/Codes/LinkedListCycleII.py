"""

142. Linked List Cycle II : https://leetcode.com/problems/linked-list-cycle-ii/

linked list가 하나 주어졌을 때, cycle이 있는지 확인하는 문제
- linked list의 cycle은 pos로 나타내며, pos는 tail이 연결되는 인덱스를 의미한다 (0-indexed)
- pos가 -1인 경우 cycle이 없다
- cycle이 있다면 시작되는 노드를, 없다면 null(None)을 리턴

Example:
- Input : head = [3,2,0,-4], pos = 1
- Output : node index 1

- Input : head = [1,2], pos = 0
- Output : node index 0

- Input : head = [1], pos = -1
- Output : None

Note:
제발 문제를 잘 읽자...
set을 이용하여 이전에 순회했던 노드로 다시 돌아가는 경우 cycle이 있으므로 해당 node를 리턴
다음 노드가 없다면 cycle이 없으므로 None을 리턴

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen, node = set(), head
        while node :
            if node in seen :
                return node
            seen.add(node)
            node = node.next
        return None