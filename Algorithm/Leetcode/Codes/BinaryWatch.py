"""

401. Binary Watch : https://leetcode.com/problems/binary-watch/

turnedOn 값이 주어졌을 때, 가능한 모든 시간을 구하는 문제
- 시간은 4개의 LED로 이루어진다 (0부터 11까지)
- 분은 6개의 LED로 이루어진다 (0부터 59까지)
- 시간은 leading zero를 포함하면 안된다 ("01:00"은 valid하지 않다)
- 분은 leading zero를 포함해야 한다 ("10:2"는 valid하지 않다)
- 결과의 순서는 상관 없다

Example:
- Input : turnedOn = 1
- Output : ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

- Input : turnedOn = 9
- Output : []

Note:
0부터 11시까지, 0부터 59분까지 모든 시간을 확인
binary 값에서 1이 turnedOn과 동일하면 결과 리스트에 추가
분은 leading zero를 포함해야 하므로 zfill을 사용

"""

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count("1") == turnedOn:
                    res.append(str(i)+":"+str(j).zfill(2))
        return res