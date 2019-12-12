"""

299. Bulls and Cows : https://leetcode.com/problems/bulls-and-cows/

secret과 guess 문자열이 주어졌을 때, 몇 개의 숫자를 맞췄는지 확인하는 문제
- bulls: 동일한 위치에 동일한 숫자가 있는 경우 (A로 표시)
- cows: 다른 위치에 동일한 숫자가 있는 경우 (B로 표시)
- secret과 guess는 모두 숫자만 포함되어 있으며, 길이는 항상 같다

Example:
- Input : secret = "1807", guess = "7810"
- Output : "1A3B"

- Input : secret = "1123", guess = "0111"
- Output : "1A1B"

Note:
문자열의 길이가 4로 보장되지 않으므로, secret에 등장하는 숫자를 미리 체크하여 dict로 관리
A(bulls)를 우선적으로 확인 후, A에 해당하지 않는 값들로 B(cows)를 확인

"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        sec, remain = {}, []
        for num in secret :
            if num in sec :
                sec[num] += 1
            else :
                sec[num] = 1
        for idx, num in enumerate(guess) :
            if secret[idx] == num :
                a += 1
                sec[num] -= 1
            else :
                remain.append(num)
        for num in remain :
            if num in sec and sec[num] >= 1 :
                b += 1
                sec[num] -= 1
        return str(a) + "A" + str(b) + "B"