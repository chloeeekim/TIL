"""

933. Number of Recent Calls : https://leetcode.com/problems/number-of-recent-calls/

아래 조건을 만족하는 RecentCounter 클래스를 완성하는 문제
- zero recent requests로 초기화된다
- ping(int t)이 실행되는 경우, [t-3000, t] 범위 내의 recent requests만 포함되며, 해당 requests의 개수를 리턴한다
- 모든 ping이 실행되는 경우, 항상 이전 call보다 큰 값의 t가 주어진다

Example:
- Input : 
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
- Output : [null, 1, 2, 3, 3]
- RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [100, 3001, 3002], range is [2,3002], return 3

Note:
매번 호출되는 ping이 이전보다 큰 값의 t가 주어진다고 하였기 때문에
가장 먼저 들어온 requests는 범위에 포함되지 않는 경우 삭제 가능

"""

class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        self.req.append(t)
        while self.req[0] < t-3000:
            del self.req[0]
        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
