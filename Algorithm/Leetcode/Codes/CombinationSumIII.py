"""

216. Combination Sum III : https://leetcode.com/problems/combination-sum-iii/

1부터 9까지의 숫자 중 k개의 숫자로 만들 수 있는 합이 n인 모든 unique한 combination을 구하는 문제
- 모든 숫자는 양의 정수이다
- 숫자는 한 번만 사용되어야 한다
- 결과는 겹치는 combination을 포함해서는 안 된다

Example:
- Input : k = 3, n = 7
- Output : [[1,2,4]]

- Input : k = 3, n = 9
- Output : [[1,2,6],[1,3,5],[2,3,4]]

Note:
- Solution 1
solve() 함수를 생성하여 recursive하게 해결
k개의 숫자를 사용하였고, 합이 n인 경우 res에 append
합이 n보다 커지거나 k보다 많은 개수의 숫자를 포함하는 경우 의미가 없음
합이 n보다 작거나 k보다 적은 개수의 숫자를 사용한 경우 일단 포함시키고 다음 값을 고려
- Solution 2
itertools의 combinations 함수를 이용
1부터 9까지 k개의 숫자로 만들 수 있는 모든 combination들을 구한 다음 합이 n이 되는 경우를 res에 append

"""

# Solution 1
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def solve(self, temp: List[int], tempsum: int, used: int, count: int) :
            if tempsum == n and count == k :
                res.append(temp)
                return
            if tempsum > n or count > k :
                return
            for num in range(used + 1, 10) :
                solve(self, temp + [num], tempsum + num, num, count + 1)
        solve(self, [], 0, 0, 0)
        return res

# Solution 2
from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        combs = combinations([i for i in range(1, 10)], k)
        for comb in combs:
            if sum(comb) == n:
                res.append(comb)
        return res