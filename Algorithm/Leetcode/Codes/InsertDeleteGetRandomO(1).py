"""

380. Insert Delete GetRandom O(1) : https://leetcode.com/problems/insert-delete-getrandom-o1/

평균적으로 O(1) 시간에 해결되는 insert, delete, getRandom 함수를 구현하는 문제
- insert(val) : val를 랜덤셋에 추가. 정상 추가 시 True를, 이미 존재하는 값인 경우 False를 리턴
- remove(val) : val를 랜덤셋에서 삭제. 정상 삭제 시 True를, 셋에 존재하지 않는다면 False를 리턴
- getRandom() : 랜덤셋에 있는 값을 랜덤하게 리턴. 각 원소들은 동일한 확률로 리턴되어야 한다

Example:
- Input : ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"] [[],[1],[2],[2],[],[1],[2],[]]
- Output : [null,true,false,true,2,true,false,2]

Note:
python의 기본 random 모듈을 사용
list로만 구현했을 때, 속도가 느린 문제가 있어 dict를 같이 사용하여 각 원소의 인덱스를 저장하는 방식으로 해결

"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = dict()
        self.value = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx :
            return False
        self.value.append(val)
        self.idx[val] = len(self.value) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idx :
            self.value[self.idx[val]] = self.value[-1]
            self.idx[self.value[-1]] = self.idx[val]
            del self.idx[val]
            del self.value[-1]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.value)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()