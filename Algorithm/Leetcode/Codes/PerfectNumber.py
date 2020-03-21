"""

507. Perfect Number : https://leetcode.com/problems/perfect-number/

주어진 숫자가 Perfect Number인지 확인하는 문제
- Perfect Number란 해당 숫자와 모든 positive divisors(자기 자신 제외)의 합이 동일한 숫자를 의미한다

Example:
- Input : 28
- Output : true
- 28 = 1 + 2 + 4 + 7 + 14

Note:
모든 positive divisors에 자기 자신은 포함되지 않으므로, 1 이하의 숫자(음수 포함)는 전부 perfect number가 아니다
해당 숫자의 sqrt까지를 확인하여 divisor라면 total에 더하는 방식

"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1 :
            return False
        total = 1
        for i in range(2, int(num ** 0.5) + 1) :
            if num % i == 0 :
                total += i
                total += num / i
                if total > num :
                    return False
        return True if total == num else False