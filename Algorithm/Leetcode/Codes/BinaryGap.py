"""

868. Binary Gap : https://leetcode.com/problems/binary-gap/

주어진 양의 정수 N을 이진수로 나타내었을 때, 1 사이의 longest distance를 구하는 문제
- 1이 두 개 이상 존재하지 않는 경우 0을 리턴한다

Example:
- Input : 22
- Output : 2
- 22 = 0b10110 -> longest distance: 101

- Input : 5
- Output : 2
- 5 = 0b101

- Input : 6
- Output : 1
- 6 = 0b110

- Input : 8
- Output : 0
- 8 = 0b1000 -> 1이 하나밖에 없으므로 longest distance를 구할 수 없다

Note:
'0b'와 같은 prefix는 필요 없으므로 format(N, 'b')를 통해 바이너리로 변환
이전에 발견된 1의 마지막 인덱스를 활용하여 각각의 1 사이의 distance를 구하는 방식

"""

class Solution:
    def binaryGap(self, N: int) -> int:
        b, gap, lastidx = format(N, 'b'), 0, 0
        for i, ch in enumerate(b):
            if ch == '1':
                gap = max(gap, i-lastidx)
                lastidx = i
        return gap