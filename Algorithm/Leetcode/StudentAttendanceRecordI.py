"""

551. Student Attendance Record I : https://leetcode.com/problems/student-attendance-record-i/

학생의 출석 정보가 문자열의 형태로 주어졌을 때, 특정 조건을 만족하는지 찾는 문제
- 문자열은 'A(Absent)', 'L(Late)', 'P(Present)' 세 가지 문자로만 구성된다
- 'A'가 한 번을 초과하는 경우 False를 리턴한다
- 연속해서 두 번 초과의 'L'이 존재하는 경우 False를 리턴한다

Example:
- Input : "PPALLP"
- Output : True

- Input : "PPALLL"
- Output : False
- 연속해서 L이 세 번 등장

Note:
absent: A가 몇 번 등장하는지를 카운트
clate: 연속된 L이 몇 번 등장하는지를 카운트. L이 아닌 다른 문자열이 나오면 0으로 초기화

"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        clate = 0
        for ch in s :
            if ch == 'A' :
                absent += 1
                clate = 0
                if absent == 2 :
                    return False
            elif ch == 'L' :
                clate += 1
                if clate >= 3 :
                    return False
            else :
                clate = 0
        return True