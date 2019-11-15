"""

77. Combinations : https://leetcode.com/problems/combinations/

두 정수 n과 k가 주어졌을 때, 1부터 n까지의 숫자를 써서 k개의 숫자로 이루어진 가능한 모든 combination들을 구하는 문제

Example:
- Input : n = 4, k = 2
- Output : [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Note:
solve() 함수를 생성하여 recursive하게 해결
중복되는 정수가 없으므로 함수가 호출될 때 생기는 모든 temp는 중복되지 않음을 보장
[1,2]와 [2,1]은 중복이므로, 이미 사용한 숫자의 앞부분(~i)은 고려할 필요가 없다

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def solve(self, temp: List[int], remain: int, count: int) :
            if count == k :
                res.append(temp)
                return
            for i in range(remain, n+1) :
                solve(self, temp + [i], i+1, count + 1)
        solve(self, [], 1, 0)
        return res