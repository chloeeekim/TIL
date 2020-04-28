"""

769. Max Chunks To Make Sorted : https://leetcode.com/problems/max-chunks-to-make-sorted/

0부터 arr.length-1까지의 숫자로 이루어진 arr이 주어졌을 때, 아래 조건을 만족하는 chunk로 나눌 수 있는 최대 개수를 구하는 문제
- 각각의 chunk를 따로 정렬했을 때, 전체 arr이 정렬되어야 한다
- arr의 길이는 [1, 10] 범위이다
- arr은 [0, 1, ... , arr.length-1]의 permutation이다

Example:
- Input : arr = [4,3,2,1,0]
- Output : 1
- chunk로 나누게 되면 정렬할 수 없다

- Input : arr = [1,0,2,3,4]
- Output : 4
- [1,0], [2], [3], [4]로 나누는 것이 가장 많이 나눌 수 있는 방법

Note:
763번 Partition Labels의 아이디어를 사용하여 해결
0부터 arr.length-1까지의 숫자로 이루어져 있으므로, 각 숫자는 위치해야 하는 인덱스를 의미
만약 숫자가 다른 곳에 위치해있다면, 실제 인덱스까지의 범위는 하나의 chunk로 구분되어야 한다

"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = temp = start = 0
        for i, num in enumerate(arr):
            temp = max(temp, num)
            if i == temp:
                count += 1
                start = i+1
        return count