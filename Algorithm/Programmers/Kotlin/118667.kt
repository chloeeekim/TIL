/*

두 큐 합 같게 만들기 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

길이가 같은 두 개의 큐가 주어졌을 때, 원소를 옮겨 각 큐의 원소 합이 같도록 만드는 최소 횟수를 구하는 문제
- 하나의 큐에서 pop하고, 다른 큐에 insert 하는 작업을 합쳐 1회 수행한 것으로 간주한다
- 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 리턴한다

Example:
- Input : queue1=[3, 2, 7, 2], queue2=[4, 6, 5, 1]
- Output : 2

- Input : queue1=[1, 2, 1, 2], queue2=[1, 10, 1, 2]
- Output : 7

- Input : queue1=[1, 1], queue2=[1, 5]
- Output : -1

Note:
합 계산 과정에서 오버플로우가 발생하는 케이스가 있으므로, Long 타입으로 계산
주어진 queue를 ArrayDeque<Long> 타입으로 변환
두 큐의 합이 짝수가 아니라면 같게 만들 수 없으므로 -1을 리턴
greedy한 방법으로 합이 큰 큐에서 removeFirst(), 합이 작은 큐에 addLast()
전체 사이즈 * 2번 이상 진행하면 초기 상태로 돌아오기 때문에 더 이상 진행해도 의미가 없다

 */

class Solution {
    fun solution(queue1: IntArray, queue2: IntArray): Int {
        var sum1 = queue1.fold(0L) { acc, n -> acc + n }
        var sum2 = queue2.fold(0L) { acc, n -> acc + n }
        val size = queue1.size + queue2.size

        if ((sum1 + sum2) % 2 != 0L) return -1

        val q1 = ArrayDeque(queue1.map { it.toLong() })
        val q2 = ArrayDeque(queue2.map { it.toLong() })

        var answer = 0
        while (answer <= size * 2) {
            when {
                sum1 == sum2 -> return answer
                sum1 > sum2 -> {
                    val temp = q1.removeFirst()
                    q2.addLast(temp)
                    sum1 -= temp
                    sum2 += temp
                }
                else -> {
                    val temp = q2.removeFirst()
                    q1.addLast(temp)
                    sum1 += temp
                    sum2 -= temp
                }
            }
            answer++
        }

        return -1
    }
}