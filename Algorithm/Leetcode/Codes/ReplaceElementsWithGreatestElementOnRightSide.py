"""

1299. Replace Elements with Greatest Element on Right Side : https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

숫자로 이루어진 리스트 arr을 다음 조건을 만족하도록 값을 변경하는 문제
- 각 인덱스를 기준으로 오른쪽에 있는 원소들의 값 중 가장 큰 값으로 해당 인덱스의 값을 변경한다
- 마지막 원소는 -1로 변경한다
- 주어지는 arr의 길이는 1 이상 10000 이하이다
- arr에 포함되는 값의 범위는 1 이상 100000 이하이다

Example:
- Input : arr = [17,18,5,4,6,1]
- Output : [18,6,6,6,1,-1]

Note:
오른쪽에서부터 시작하여 해당 인덱스 이전까지의 최대값을 tempmax에 저장
해당 인덱스의 값을 tempmax로 변경하고, tempmax의 값을 갱신

"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tempmax, arr[-1] = arr[-1], -1
        for i in range(len(arr)-2, -1, -1):
            tempmax, arr[i] = max(tempmax, arr[i]), tempmax
        return arr