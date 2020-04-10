"""

876. Middle of the Linked List : https://leetcode.com/problems/middle-of-the-linked-list/

비어 있지 않은 singly linked list가 주어졌을 때, 가운데 있는 노드를 구하는 문제
- 중간에 위치한 노드가 두 개라면(전체 길이가 짝수인 경우) 두 번째 중간 노드를 리턴한다

Example:
- Input : [1,2,3,4,5]
- Output : [3,4,5]

- Input : [1,2,3,4,5,6]
- Output : [4,5,6]
- 중간에 위치한 노드가 두 개(3,4)인 경우 두 번째 노드를 리턴

Note:
노드 정보를 리스트에 저장하는 방식으로 해결
인덱스가 0부터 시작하므로 중간에 위치한 노드는 리스트의 길이 // 2로 구할 수 있다

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodes, node = [], head
        while node:
            nodes.append(node)
            node = node.next
        return nodes[len(nodes)//2]