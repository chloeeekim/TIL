"""

n + 1 카드게임 : https://school.programmers.co.kr/learn/courses/30/lessons/258707

1 ~ n 사이의 수가 적힌 순서가 정해진 카드 뭉치와 coin 개의 동전이 주어졌을 때, 도달 가능한 최대 라운드를 구하는 문제
- 게임 진행 방식은 다음과 같다
    - 처음에 카드 뭉치에서 카드 n/3 장을 뽑아 모두 가진다 (n은 6의 배수이다)
    - 각 라운드가 시작할 때, 카드를 두 장 뽑으며, 카드 뭉치에 남은 카드가 없다면 게임을 종료한다
    - 뽑은 카드는 한 장당 동전 하나를 소모해 가지거나, 동전을 소모하지 않고 버릴 수 있다
    - 카드에 적힌 수의 합이 n+1이 되도록 카드 두 장을 내놓고 다음 라운드로 진행할 수 있다
    - 만약 카드 두 장을 낼 수 없다면, 게임을 종료한다
- coin은 0 이상 n 이하인 정수이다
- cards의 길이는 6 이상 1,000 미만인 6의 배수이다
- cards[i]는 i+1번째로 뽑는 카드에 적힌 수를 의미하며, cards의 원소는 중복되지 않는다

Example:
- Input : coin=4, cards=[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
- Output : 5

- Input : coin=3, cards=[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
- Output : 2

- Input : coin=2, cards=[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
- Output : 4

- Input : coin=10, cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- Output : 1

Note:
이전에 뽑은 카드가 이후 라운드에서 필요하게 될 수도 있으므로, temp에 모아두고 필요 시 확인
다음 순서로 진행된다
    1. 뽑은 카드가 가지고 있는 카드와 n+1 합을 만들 수 있고, hands에 추가한다 (코인 1개 소모)
    1-1. 뽑은 카드가 가지고 있는 카드와 합을 만들 수 없다면, 일단 temp에 넣어둔다
    2. hands에 있는 카드들로 n+1 합이 만들어지는지 확인한다
    2-1. hands에 있는 카드로 안 되는 경우, hands에 있는 카드 + temp에 있는 카드로 합이 만들어지는지 확인한다 (코인 1개 소모)
    2-2. 마지막으로 temp에 있는 카드들로 합이 만들어지는지 확인한다 (코인 2개 소모)
    3. 어떤 방법으로도 합이 만들어지지 않는다면 결과를 리턴한다
    4. 모든 카드를 다 뽑게 되면 게임이 종료된다

"""

def solution(coin, cards):
    n = len(cards)
    hands, idx = cards[:n//3], n//3
    temp = []
    result = 1

    while idx < n:
        pick = cards[idx:idx+2]
        idx += 2

        for p in pick:
            if n + 1 - p in hands and coin:
                hands.append(p)
                coin -= 1
            else:
                temp.append(p)

        match1 = False
        for h in hands:
            if n + 1 - h in hands:
                match1 = True
                hands.remove(h)
                hands.remove(n + 1 - h)
                result += 1
                break

        if not match1:
            match2 = False
            for t in temp:
                if n + 1 - t in hands and coin:
                    match2 = True
                    hands.remove(n + 1 - t)
                    temp.remove(t)
                    coin -= 1
                    result += 1
                    break
            if not match2:
                for t in temp:
                    if n + 1 - t in temp and coin >= 2:
                        temp.remove(t)
                        temp.remove(n + 1 - t)
                        coin -= 2
                        result += 1
                        break
                else:
                    return result
    return result