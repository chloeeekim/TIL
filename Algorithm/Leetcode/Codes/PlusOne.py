"""

66. Plus One : https://leetcode.com/problems/plus-one/

비어 있지 않은, 숫자로 이루어진 리스트가 하나 주어졌을 때,
리스트의 값이 나타내는 정수에 1을 더한 값을 리스트로 리턴하는 문제
- 숫자는 음수가 아니며, 0으로 시작하지 않는다
- 리스트 내의 각각의 원소들은 single digit을 나타낸다
- most significant digit가 리스트의 가장 앞에 저장된다

Example:
- Input : [1,2,3]
- Output : [1,2,4]
- [1,2,3]은 정수 123을 의미하므로, 1을 더한 값은 124

- Input : [4,3,2,1]
- Output : [4,3,2,2]
- [4,3,2,1]은 정수 4321을 의미하므로, 1을 더한 값을 4322

Note:
reversed : 리스트 순서를 거꾸로 뒤집음
insert(0, value)를 이용하여 리스트의 가장 앞에 계산한 값이 포함되도록 함
자릿수가 바뀌는 경우(ex. 99 -> 100)를 대비하여 마지막에 up이 남아있는지 확인

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        up = 1
        for i in reversed(digits) :
            if i + up >= 10 :
                res.insert(0, 0)
                up = 1
            else :
                res.insert(0, i + up)
                up = 0
        if up == 1 :
            res.insert(0, 1)
        return res