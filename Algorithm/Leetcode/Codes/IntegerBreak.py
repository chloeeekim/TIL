"""

343. Integer Break : https://leetcode.com/problems/integer-break/

양의 정수 n이 주어졌을 때, 이를 적어도 2개 이상의 정수의 합으로 나누고, 이 정수들의 최대곱을 구하는 문제
- n은 2 이상 58 이하이다

Example:
- Input : 2
- Output : 1
- 2 = 1 + 1이므로, 1 x 1 = 1

- Input : 10
- Output : 36
- 10 = 3 + 3 + 4, 3 x 3 x 4 = 36

Note:
특정 값을 여러 정수들의 합으로 나누었을 때 구할 수 있는 최대곱을 리스트에 저장하는 방식 (dp)
n을 a+b로 나눈다고 가정하면, n으로 구할 수 있는 최대곱은
a(b)로 구할 수 있는 최대곱 x b(a) 혹은 a x b가 된다

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        arr = [0,0,1] + [0 for _ in range(n-2)]
        for i in range(3, n+1):
            maxpro = 0
            for j in range(1, i-1):
                maxpro = max(maxpro, j * (i-j))
                maxpro = max(maxpro, arr[j] * (i-j))
            arr[i] = maxpro
        return arr[n]