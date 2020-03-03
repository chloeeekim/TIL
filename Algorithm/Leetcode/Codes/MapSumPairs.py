"""

677. Map Sum Pairs : https://leetcode.com/problems/map-sum-pairs/

MapSum class를 구현하는 문제
- insert method : (key, value)로 (string, integer) 쌍이 입력
- sum method : prefix로 시작하는 key의 값들의 합을 리턴

Example:
- Input : ["MapSum", "insert", "sum", "insert", "sum"], [[], ["apple",3], ["ap"], ["app",2], ["ap"]]
- Output : [null,null,3,null,5]

Note:
dict를 생성하여 입력된 key, value pair를 관리

"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for st in self.dict :
            if st.startswith(prefix) :
                res += self.dict[st]
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)