"""

141. Linked List Cycle : https://leetcode.com/problems/linked-list-cycle/

linked list가 하나 주어졌을 때, cycle이 있는지 확인하는 문제
- linked list의 cycle은 pos로 나타내며, pos는 tail이 연결되는 인덱스를 의미한다 (0-indexed)
- pos가 -1인 경우 cycle이 없다

Example:
- Input : head = [3,2,0,-4], pos = 1
- Output : true

- Input : head = [1,2], pos = 0
- Output : true

- Input : head = [1], pos = -1
- Output : false

Note:
set을 이용
이전에 순회했던 노드로 다시 돌아가는 경우 cycle이 있다고 판단
다음 노드가 없다면 cycle이 없다

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen, node = set(), head
        while node :
            if node in seen :
                return True
            seen.add(node)
            node = node.next
        return False