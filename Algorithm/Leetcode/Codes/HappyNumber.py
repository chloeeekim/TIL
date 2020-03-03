"""

202. Happy Number : https://leetcode.com/problems/happy-number/

양의 정수 하나가 주어졌을 때, 해당 숫자가 happy number인지 확인하는 문제
- happy number : 각 자릿수의 제곱을 더한 값을 구하는 방식을 반복했을 때, 1이 나오는 숫자
- happy number가 아니라면 위 방식을 반복했을 때, 1을 포함하지 않는 숫자들의 cycle이 반복된다

Example:
- Input : 19
- Output : true
- 1^2 + 9^2 = 82 / 8^2 + 2^2 = 68 / 6^2 + 8^2 = 100 / 1^2 + 0^2 + 0^0 = 1

Note:
반복되는지를 확인하기 위하여 seen 리스트를 사용
이전에 나왔었던 숫자가 나온다면 happy number가 아님

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        num = n
        while True :
            nxt = 0
            while num != 0 :
                nxt += (num % 10) ** 2
                num = num // 10
            if nxt == 1 :
                return True
            if nxt in seen :
                return False
            else :
                seen.append(nxt)
                num = nxt
        return False