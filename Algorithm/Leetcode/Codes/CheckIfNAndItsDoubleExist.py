"""

1346. Check If N and Its Double Exist : https://leetcode.com/problems/check-if-n-and-its-double-exist/

정수들이 포함된 리스트 arr이 주어졌을 때, N과 N의 두 배가 되는 M이 모두 arr에 존재하는지 확인하는 문제
- i != j 인 arr[i]가 arr[j]의 두 배가 되는 경우를 의미한다 (i == j인 경우는 고려하지 않는다)
- arr의 길이는 2 이상 500 이하이다
- arr에 포함된 원소의 값은 -1000 이상 1000 이하이다

Example:
- Input : arr = [10,2,5,3]
- Output : true
- 5와 10이 조건을 만족한다

- Input : arr = [7,1,14,11]
- Output : true
- 7과 14가 조건을 만족한다

- Input : arr = [3,1,7,11]
- Output : false

Note:
리스트를 순회하면서 발견한 원소는 seen dict에 추가
seen에 해당 값의 2배가 되는 값이 있거나, 절반이 되는 값이 있다면 true
마지막 원소까지 조건을 만족하는 값이 없다면 false

"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        for num in arr:
            if num*2 in seen or num/2 in seen:
                return True
            seen[num] = 1
        return False