""

989. Add to Array-Form of Integer : https://leetcode.com/problems/add-to-array-form-of-integer/

리스트의 형태로 주어지는 숫자 num과 숫자 k를 더한 값을 리스트의 형태로 반환하는 문제
- num이 1321이라면 [1,3,2,1]의 형태로 주어진다
- num은 0으로 시작하지 않으며, 1 이상이다

Example:
- Input : num = [1,2,0,0], k = 34
- Output : [1,2,3,4]

- Input : num = [2,7,4], k = 181
- Output : [4,5,5]

- Input : num = [2,1,5], k = 806
- Output : [1,0,2,1]

- Input : num = [9,9,9,9,9,9,9,9,9,9], k = 1
- Output : [1,0,0,0,0,0,0,0,0,0,0]

Note:
리스트의 형태로 주어진 num을 숫자로 변환하여 k와 더하기 계산
다시 string에서 리스트로 변환
참고) 더 나은 방법?

"""

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = 0
        for n in num:
            temp *= 10
            temp += n            
        tstr, res = str(temp+k), []
        for t in tstr:
            res.append(t)
        return res