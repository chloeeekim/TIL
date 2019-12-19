"""

481. Magical String : https://leetcode.com/problems/magical-string/

Magical String의 앞 n개의 숫자에 1이 몇 개가 포함되는지 찾는 문제
- Magical String: 1과 2로 이루어져 있으며, 연속된 숫자의 빈도를 나열하면 원래의 숫자열이 되는 숫자열
- 예: S = "1221121221221121122..."
- n은 100,000을 넘지 않는다

Example:
- Input : 6
- Output : 3
- "122112"가 되므로, 1의 개수는 3

Note:
앞의 숫자가 뒤에 등장하는 숫자열을 결정짓는 형태
magical string을 만들어가면서 전체 길이가 구하고자 하는 n보다 크거나 같아지면 중단
속도를 위해 문자열 대신 list로 구현

"""

class Solution:
    def magicalString(self, n: int) -> int:
        idx, total, magical, before = 3, 5, [1,2,2,1,1], 1
        while total <= n :
            repeat = magical[idx]
            before = 1 if before == 2 else 2
            magical += [before] * repeat
            idx += 1
            total += repeat
        return magical[:n].count(1)