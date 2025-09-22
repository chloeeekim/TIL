"""

크레인 인형뽑기 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/64061

n x n 크기의 정사각 격자 내의 인형들의 정보와 크레인을 작동시키는 순서가 주어졌을 때, 터뜨려져 사라진 인형의 개수를 구하는 문제
- 모든 인형은 1 x 1 크기의 격자 한 칸을 차지하며, 격자의 가장 아래 칸부터 차곡차곡 쌓여 있다
- 크레인을 사용하면 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있다
- 집어올린 인형은 바구니에 쌓이며, 이 때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓인다
- 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라진다
- 크레인 작동 시 인형이 집어지지 않는 경우는 없다
- 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무 일도 일어나지 않는다
- 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정한다
- board는 격자의 상태가 담긴 2차원 배열로, 크기는 5 x 5 이상 30 x 30 이하이다
    - board의 각 칸에는 0 이상 100 이하인 정수가 담겨 있다
    - 0은 빈 칸을 나타내며, 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미한다
- moves 배열은 크기 1 이상 1,000 이하인 정수 배열이며, 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수이다

Example:
- Input : board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves=[1,5,3,5,1,2,1,4]
- Output : 4

Note:
stack을 사용하여 바구니 내에서 터뜨려져 사라지는 경우를 확인

"""

def solution(board, moves):
    n = len(board)
    stack = []
    count = 0

    for move in moves:
        idx = 0
        while idx < n:
            doll = board[idx][move - 1]
            if doll == 0:
                idx += 1
            else:
                board[idx][move - 1] = 0
                if stack and stack[-1] == doll:
                    stack.pop()
                    count += 2
                else:
                    stack.append(doll)
                break
    return count
