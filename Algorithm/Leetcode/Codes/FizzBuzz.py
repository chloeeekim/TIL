"""

412. Fizz Buzz : https://leetcode.com/problems/fizz-buzz/

1부터 n까지의 숫자를 특정한 규칙에 따라 문자열의 리스트로 바꾸는 문제
- 3의 배수인 경우 "Fizz"로 표시
- 5의 배수인 경우 "Buzz"로 표시
- 3과 5의 공배수인 경우 "FizzBuzz"로 표시

Example:
- Input : 15
- Output : ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Note:
15로 나누어 떨어지는 경우, 5로 나누어 떨어지는 경우, 3으로 나누어 떨어지는 경우로 확인

"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1) :
            if i % 15 == 0 :
                res.append("FizzBuzz")
            elif i % 5 == 0 :
                res.append("Buzz")
            elif i % 3 == 0 :
                res.append("Fizz")
            else :
                res.append(str(i))
        return res