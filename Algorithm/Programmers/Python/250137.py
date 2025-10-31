"""

[PCCP 기출문제] 1번 / 붕대 감기 : https://school.programmers.co.kr/learn/courses/30/lessons/250137

붕대 감기 기술의 정보와 몬스터의 공격 패턴이 주어졌을 때, 모든 공격이 끝난 직후 남은 체력을 구하는 문제
- 붕대 감기는 t초 동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복하며, t초 연속으로 붕대를 감는 데 성공하면 y만큼의 체력을 추가로 회복한다
- 최대 체력 health 이상으로 현재 체력이 커지는 것은 불가능하다
- 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없다
- 기술이 취소당하거나 기술이 끝난면 그 죽시 붕대 감기를 다시 사용하며, 연속 성공 시간은 0으로 초기화된다
- 몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어들며, 현재 체력이 0 이하가 되면 캐릭터가 사망한다
- 공격을 받는 도중 캐릭터가 사망하면 -1을 리턴한다

Example:
- Input : bandage=[5,1,5], health=30, attacks=[[2,10],[9,15],[10,5],[11,5]]
- Output : 5

- Input : bandage=[3,2,7], health=20, attacks=[[1,15],[5,16],[8,6]]
- Output : -1

- Input : bandage=[4,2,7], health=20, attacks=[[1,15],[5,16],[8,6]]
- Output : -1

- Input : bandage=[1,1,1], health=5, attacks=[[1,2],[3,2]]
- Output : 3

Note:
몬스터의 공격 사이에 회복되는 체력은 min(health, 현재 체력 + 시간 * 회복량 + 연속 성공 횟수 * 추가 회복량)이 된다

"""

def solution(bandage, health, attacks):
    curr_health, curr_time = health, 0
    for [time, damage] in attacks:
        duration = time - curr_time - 1
        success = duration // bandage[0]
        curr_health = min(health, curr_health + duration * bandage[1] + success * bandage[2])
        curr_health -= damage
        curr_time = time

        if curr_health <= 0:
            return -1
    return curr_health