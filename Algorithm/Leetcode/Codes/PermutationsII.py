"""

47. Permutations II : https://leetcode.com/problems/permutations-ii/

중복되는 숫자가 포함된 리스트가 주어졌을 때, 이를 이용해 만들 수 있는 모든 permutation들을 구하는 문제

Example:
- Input : [1,1,2]
- Output : [[1,1,2],[1,2,1],[2,1,1]]

Note:
rec() 함수를 생성하여 recursive하게 해결
앞에서 만들어진 리스트(temp)와 남은 리스트(remain)를 관리
Permutation 문제에서 사용한 함수를 변경
추가) 다른 최적화 방법 찾기. 현재 알고리즘은 속도가 너무 느리다는 단점

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(self, temp: List[int], remain: List[int]):
            if not remain :
                if temp not in res :
                    res.append(temp)
                return
            seen = remain[0] - 1
            for i, num in enumerate(remain) :
                if num != seen :
                    rem = remain[:i] + remain[i+1:]
                    rec(self, temp + [num], rem)
                    seen = num
        rec(self, [], nums)
        return res