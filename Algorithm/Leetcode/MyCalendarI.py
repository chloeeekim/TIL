"""

729. My Calendar I : https://leetcode.com/problems/my-calendar-i/

각 이벤트의 시작 날짜와 종료 날짜가 주어졌을 때, 더블 부킹 여부를 확인하는 문제
- 다른 이벤트와 겹치는 경우 False를 리턴하고, 이벤트가 추가되지 않는다
- 시작 날짜는 포함되며, 종료 날짜는 포함되지 않는다 ([start, end)로 이벤트가 진행된다)
- 시작 날짜와 종료 날짜는 동일하게 주어지지 않는다 (start <= x < end)
- book 함수는 테스트 케이스당 최대 1000번까지 호출된다
- start와 end는 각각 [0, 10^9] 범위이다

Example:
- Input : ["MyCalendar","book","book","book"] [[],[10,20],[15,25],[20,30]]
- Output : [null,true,false,true]

Note:
단순하게 기존 예약과의 숫자 비교를 통해 확인하는 방법
기존에 존재하는 예약의 시작 날짜가 해당 이벤트의 이후거나, 종료 날짜가 해당 이벤트의 이전이면 확인할 필요가 없음
해당 이벤트의 시작 날짜나 종료 날짜가 기존 예약의 범위 이내인 경우 무조건 겹치게 되므로 False를 리턴
시작 날짜가 겹치지 않는 경우 종료 날짜가 기존 예약의 시작 이후라면 겹치게 되고,
종료 날짜가 겹치지 않는 경우 시작 날짜가 기존 예약의 종료 이전이라면 겹치게 되므로 False를 리턴

"""

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:  
        for [bstart, bend] in self.bookings :
            if bstart >= end or bend <= start :
                continue
            if start >= bstart and start < bend :
                return False
            elif end > bstart :
                return False
            if end > bstart and end <= bend :
                return False
            elif start < bend :
                return False
        self.bookings.append([start, end])
        return True            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)