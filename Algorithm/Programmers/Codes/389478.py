"""

택배 상자 꺼내기 : https://school.programmers.co.kr/learn/courses/30/lessons/389478

n개의 택배 상자가 가로로 w개씩 쌓여 있을 때, 주어진 번호의 상자를 꺼내기 위해서 몇 개의 택배 상자를 꺼내야 하는지 구하는 문제
- 왼쪽에서 오른쪽으로 가면서 1번부터 상자를 순서대로 놓고, 그 위층에는 오른쪽에서 왼쪽으로, 다시 그 위층에는 왼쪽에서 오른쪽으로 놓는 방식으로 진행된다
- 택배 상자를 꺼내기 위해서는 위에 있는 모든 상자를 꺼내야 한다
- 꺼내야 하는 택배 상자의 번호 num은 전체 택배 상자의 개수 n보다 작거나 같다

Example:
- Input : n=22, w=6, num=8
- Output : 3
- 20, 17, 8번 순서로 꺼내야 한다

- Input : n=13, w=3, num=6
- Output : 4
- 13, 12, 7, 6번 순서로 꺼내야 한다

Note:
전체(top)와 꺼내야 하는 상자(pick)의 높이와 왼쪽에서 몇 번째에 위치하는지 등을 계산
층이 홀수번째인지 짝수번째인지에 따라 반대로 계산한다

"""

def solution(n, w, num):
    top_h, top_w = n // w, n % w
    pick_h, pick_w = num // w, num % w

    top_h = top_h + 1 if top_w != 0 else top_h
    pick_h = pick_h + 1 if pick_w != 0 else pick_h
    top_w = w if top_w == 0 else top_w
    pick_w = w if pick_w == 0 else pick_w

    pick_left = pick_w if pick_h % 2 == 1 else w - pick_w + 1
    top_left = top_w if top_h % 2 == 1 else w - top_w + 1

    result = top_h - pick_h + 1
    if top_h % 2 == 1:
        result = result - 1 if pick_left > top_left else result
    else:
        result = result - 1 if pick_left < top_left else result
    return result