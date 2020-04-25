"""

728. Self Dividing Numbers : https://leetcode.com/problems/self-dividing-numbers/

주어진 범위 내에서 self-dividing number를 모두 구하는 문제
- self-dividing number란 해당 숫자가 각 자릿수로 모두 나누어지는 숫자를 의미한다
- 128의 경우 128이 1, 2, 8 모두 나누어떨어지므로 self-dividing number가 된다
- 숫자에 0이 포함된 경우는 self-dividing number가 아니다

Example:
- Input : left = 1, right = 22
- Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
해당 숫자가 self-dividing number인지를 판별하는 isdividing() 함수를 생성하여 해결
사실 함수로 빼지 않고 for 문 안에 추가하여도 상관 없음
10으로 나눈 나머지가 자릿수가 되므로 mod를 계속 구해 나가면서 나누어떨어지는지 확인

"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isdividing(num: int) -> bool:
            temp = num
            while temp > 0:
                temp, mod = divmod(temp, 10)
                if mod == 0 or num % mod != 0:
                    return False
            return True
        res = []
        for i in range(left, right+1):
            if isdividing(i):
                res.append(i)
        return res