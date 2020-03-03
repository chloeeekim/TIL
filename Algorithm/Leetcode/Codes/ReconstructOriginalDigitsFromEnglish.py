"""

423. Reconstruct Original Digits from English : https://leetcode.com/problems/reconstruct-original-digits-from-english/

0부터 9까지의 숫자를 나타내는 알파벳이 마구잡이로 섞인 문자열이 주어졌을 때, 원래의 숫자를 찾는 문제
- 숫자는 오름차순으로 정렬하여 나타내어야 한다
- 입력은 모두 lowercase 알파벳으로 주어진다
- 입력은 모두 valid하며 원본 숫자로 바꿀 수 있다 ("abc"나 "zerone" 같은 경우는 존재하지 않는다)
- 입력의 길이는 50000 이하이다

Example:
- Input : "owoztneoer"
- Output : "012"

- Input : "fviefuro"
- Output : "45"

Note:
zero의 z 같이 하나의 알파벳으로 숫자를 특정 지을 수 있는 경우를 고려하여 계산해야 하는 순서를 order로 미리 정의
주어진 문자열에 포함되는 알파벳들의 갯수를 확인하여 계산
참고) 더 빠르게 해결하는 방법?

"""

class Solution:
    def originalDigits(self, s: str) -> str:
        digits = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        order = {'z':0, 'x':6, 'g':8, 'w':2, 's':7, 'v':5, 'f':4, 'o':1, 't':3, 'i':9}
        include, res = {}, [0 for _ in range(10)]
        for ch in s :
            if ch in include :
                include[ch] += 1
            else :
                include[ch] = 1
        for key, value in order.items() :
            if key in include :
                temp = include[key]
                if temp == 0 :
                    continue
                res[value] = temp
                for ch in digits[value] :
                    include[ch] -= temp
        resstr = ""
        for i in range(10) :
            resstr += str(i) * res[i]
        return resstr