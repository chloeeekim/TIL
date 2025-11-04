/*

디펜스 게임 : https://school.programmers.co.kr/learn/courses/30/lessons/142085

처음 보유한 병사의 수, 사용 가능한 무적권의 수, 매 라운드마다 공격해오는 적의 수가 주어졌을 때, 최대 몇 라운드까지 막을 수 있는지 구하는 문제
- 디펜스 게임은 다음과 같은 규칙으로 진행된다
    - 처음에 병사 n명을 가지고 시작한다
    - 매 라운드마다 enemy[i]마리의 적이 등장한다
    - 남은 병사 중 enemy[i]명만큼 소모하여 enemy[i]마리의 적을 막을 수 있다
        - 만약 남은 병사의 수보다 현재 라운드의 적의 수가 더 많으면 게임이 종료된다
    - 무적권을 사용하면 병사의 소모 없이 한 라운드의 공격을 막을 수 있다
        - 무적권은 최대 k번 사용할 수 있다
- 처음 가지고 있는 병사의 수 n은 1 이상 1,000,000,000 이하이다
- 사용 가능한 무적권의 수는 1 이상 500,000 이하이다
- 매 라운드마다 공격해오는 적의 수가 담긴 정수 배열 enemy의 길이는 1 이상 1,000,000 이하이다
    - enemy[i]는 1 이상 1,000,000 이하의 정수이다
- 모든 라운드를 막을 수 있는 경우에는 enemy의 길이를 리턴한다

Example:
- Input : n=7, k=3, enemy=[4, 2, 4, 5, 3, 3, 1]
- Output : 5

- Input : n=2, k=4, enemy=[3, 3, 3, 3]
- Output : 4

Note:
최대힙을 구현하기 위해 PriorityQueue에 Collections.reverseOrder()를 사용
적의 수가 병사의 수보다 많은 경우, k가 남아 있다면 무적권을 사용
무적권을 사용할 때는 병사의 수가 가장 많은 라운드에 사용하는 것이 유리하므로 heap에서 pop한 값을 사용한다

 */

import java.util.*

class Solution {
    fun solution(n: Int, k: Int, enemy: IntArray): Int {
        if (enemy.size <= k) return enemy.size

        val heap = PriorityQueue<Int>(Collections.reverseOrder())
        var total = 0
        var remainK = k
        var answer = 0

        for (num in enemy) {
            heap.add(num)
            total += num

            if (total > n) {
                if (remainK == 0) break
                else {
                    total -= heap.poll()
                    remainK--
                }
            }

            answer++
        }

        return answer
    }
}