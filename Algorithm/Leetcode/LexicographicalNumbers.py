"""

386. Lexicographical Numbers : https://leetcode.com/problems/lexicographical-numbers/

숫자 n이 주어졌을 때, 1부터 n까지의 숫자를 lexicographical order로 나타내는 문제
- n은 최대 5,000,000까지 주어질 수 있다

Example:
- Input : 13
- Output : [1,10,11,12,13,2,3,4,5,6,7,8,9]

Note:
- Solution 1
solve() 함수를 생성하여 recursive하게 해결하는 방법
lexicographical order로 순서대로 생성하여 결과 리스트에 append
- Solution 2
1부터 n까지의 숫자를 string으로 변환하여 이를 sorted

"""

# Solution 1

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def solve(self, temp: int, num: int) :
            temp = temp * 10 + num
            if temp > n :
                return
            res.append(temp)
            for i in range(10) :
                solve(self, temp, i)
        for i in range(1, 10) :
            solve(self, 0, i)
        return res

# Solution 2

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n+1)]
        return sorted(res)