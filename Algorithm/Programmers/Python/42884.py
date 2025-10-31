"""

단속카메라 : https://school.programmers.co.kr/learn/courses/30/lessons/42884

고속도로를 이동하는 차량의 경로가 주어졌을 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지 구하는 문제
- 차량의 대수는 1대 이상 10,000대 이하이다
- routes에는 차량의 이동 경로가 포함되어 있다
    - routes[i][0]은 i번째 차량이 고속도로에 진입한 지점, routes[i][1]은 차량이 고속도로에서 나간 지점을 의미한다
    - 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하이다
- 차량의 진입, 진출 지점에 카메라가 설치되어 있어도 카메라를 만난 것으로 간주한다

Example:
- Input : routes=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
- Output : 2

Note:
차량의 진출 지점을 기준으로 정렬
다음 차량의 진입 지점이 이전 차량의 진출 지점보다 크다면 단속 카메라가 한 대 더 필요하다

"""

def solution(routes):
    sroutes = sorted(routes, key=lambda x: (x[1]))
    count = 0
    end = -30001

    for cin, cout in sroutes:
        if cin > end:
            count += 1
            end = cout

    return count