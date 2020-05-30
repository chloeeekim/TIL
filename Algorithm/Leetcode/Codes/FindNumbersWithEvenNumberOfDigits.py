"""

1295. Find Numbers with Even Number of Digits : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

정수로 이루어진 리스트가 주어졌을 때, 숫자의 개수가 짝수 개인 원소의 갯수를 구하는 문제
- 주어진 리스트의 길이는 1 이상 500 이하이다
- 리스트에 포함된 원소는 1 이상 10^5 이하이다

Example:
- Input : nums = [12,345,2,6,7896]
- Output : 2
- 12와 7896이 각각 2개와 4개로 짝수 개의 숫자를 지니는 원소이다

- Input : nums = [555,901,482,1771]
- Output : 1

Note:
숫자를 문자열로 변환한 후, 문자열의 길이로 숫자의 개수를 확인하는 방법

"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count += 1 if len(str(num))%2 == 0 else 0
        return count