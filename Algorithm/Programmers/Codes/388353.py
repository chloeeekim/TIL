"""

지게차와 크레인 : https://school.programmers.co.kr/learn/courses/30/lessons/388353

컨테이너가 2차원 배열 형태로 놓여 있을 때, 요청을 순서대로 처리한 후 남은 컨테이너의 수를 구하는 문제
- "A"처럼 알파벳 하나만 요청으로 들어온 경우, 요청이 들어온 순간 접근 가능한 컨테이너를 제거
- "BB"처럼 알파벳이 두 번 반복된 경우, 요청된 종류의 모든 컨테이너를 제거

Example:
- Input : storage=["AZWQY", "CAABX", "BBDDA", "ACACA"], requests=["A", "BB", "A"]
- Output : 11

- Input : storage=["HAH", "HBH", "HHH", "HAH", "HBH"], requests=["C", "B", "B", "B", "B", "H"]
- Output : 4

Note:
storage의 사방으로 한 칸씩 0(외부)으로 패딩한 arr 생성
bfs 방식으로 접근 가능 여부 배열인 can_access를 구하는 방식

"""

def solution(storage, requests):
    n, m = len(storage) + 2, len(storage[0]) + 2
    arr = [['0'] * m for _ in range(n)]
    for i in range(n-2):
        for j in range(m-2):
            arr[i+1][j+1] = storage[i][j]
    remain = (n-2) * (m-2)
    nears = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def get_access():
        can_access = [[False] * m for _ in range(n)]
        can_access[0][0] = True
        queue = [(0, 0)]

        while queue:
            q = queue.pop(0)
            for near in nears:
                ni, nj = q[0] + near[0], q[1] + near[1]
                if ni < 0 or ni > n - 1 or nj < 0 or nj > m - 1:
                    continue
                if arr[ni][nj] == '0' and can_access[ni][nj] == False:
                    can_access[ni][nj] = True
                    queue.append((ni, nj))
        return can_access

    def remove(request, access):
        count = 0
        can_access = get_access()
        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j] == request:
                    if access == True:
                        if any(can_access[i+near[0]][j+near[1]] for near in nears):
                            count += 1
                            arr[i][j] = '0'
                    else:
                        count += 1
                        arr[i][j] = '0'
        return count

    for request in requests:
        remain -= remove(request[0], True if len(request) == 1 else False)

    return remain