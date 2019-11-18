"""

146. LRU Cache : https://leetcode.com/problems/lru-cache/

Least Recently Used (LRU) Cache를 구현하는 문제
- get, put 함수를 구현
- get(key) : cache에 key가 있으면 value를 리턴하고, 없으면 -1을 리턴
- put(key, value) : key에 해당하는 value를 set하거나 insert. cache의 capacity에 다다르면 least recently used item을 삭제하고 추가한다

Example:
- Input : ["LRUCache","put","put","get","put","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
- Output : [null,null,null,1,null,-1,null,-1,3,4]
- put(3,3)에서 key 2 삭제, put(4,4)에서 key 1 삭제

Note:
dict 사용 (key : 출현한 문자 / value : 인덱스)
느릴 것이라 생각했으나 생각보다 빨라서 조금은 당황. 99.10%

"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache :
            temp = self.cache[key]
            del self.cache[key]
            self.cache[key] = temp
            return temp
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            del self.cache[key]
            self.cache[key] = value
        else :
            if len(self.cache) >= self.capacity :
                for i in self.cache :
                    del self.cache[i]
                    break
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)