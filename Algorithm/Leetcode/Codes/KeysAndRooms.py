"""

841. Keys and Rooms : https://leetcode.com/problems/keys-and-rooms/

N개의 room이 있고, 각 방마다 열쇠가 들어있을 때, 모든 방을 다 열 수 있는지 확인하는 문제
- 0번째 방을 제외한 모든 방은 처음에 다 잠겨 있다

Example:
- Input : [[1],[2],[3],[]]
- Output : true
- 1, 2, 3번째 방을 모두 순서대로 방문할 수 있다

- Input : [[1,3],[3,0,1],[2],[0]]
- Output : false
- 2번째 방을 방문할 수 없다

Note:
얻을 수 있는 key를 queue에 넣은 후, 각 방의 방문 여부를 확인
방문한 방은 값을 1로 변경하므로, 리스트의 sum이 길이와 동일하면 모든 방을 방문한 것

"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys, entered = [0], [1] + [0 for _ in range(len(rooms)-1)]
        while keys:
            key = keys.pop(0)
            for k in rooms[key]:
                if entered[k] == 0:
                    keys.append(k)
                    entered[k] = 1
        return True if sum(entered) == len(rooms) else False