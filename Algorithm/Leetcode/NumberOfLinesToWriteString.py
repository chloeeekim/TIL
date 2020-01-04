"""

806. Number of Lines To Write String : https://leetcode.com/problems/number-of-lines-to-write-string/

주어진 문자열 S를 왼쪽에서 오른쪽으로 채워가며 쓴다고 했을 때, 몇 줄에 쓸 수 있는지 구하는 문제
- 각 알파벳에 해당하는 유닛의 크기가 리스트의 형태로 주어진다
- 한 줄에 나타낼 수 있는 최대 크기는 100이다
- 하나의 유닛은 다음 라인으로 넘어갈 수 없다 (한 줄에 100이 채워지지 않더라도 다음 라인으로 넘어갈 수 있다)
- 몇 줄에 나타낼 수 있는지와 마지막 줄에 포함되는 유닛의 크기를 리턴

Example:
- Input : widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "abcdefghijklmnopqrstuvwxyz"
- Output : [3, 60]

- Input : widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], S = "bbbcccdddaaa"
- Output : [2, 4]

Note:
각 알파벳에 해당하는 숫자(순서대로 0부터 25)를 빠르게 구하기 위해 set으로 미리 정의
현재 라인의 너비와 알파벳의 크기를 더했을 때 100이 넘는 경우, 해당 알파벳은 다음 라인에 작성되어야 한다

"""

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 
                    'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 
                    'v': 21, 'w':22, 'x':23, 'y':24, 'z':25}
        lines, width = 1, 0
        for ch in S :
            temp = widths[alphabet[ch]]
            if temp + width > 100 :
                lines += 1
                width = temp
            else :
                width += temp
        return [lines, width]