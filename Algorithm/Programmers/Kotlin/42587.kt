/*

프로세스 : https://school.programmers.co.kr/learn/courses/30/lessons/42587

실행 대기 큐에 있는 프로세스들의 중요도가 주어졌을 때, 특정 프로세스가 몇 번째로 실행되는지 구하는 문제
- 운영체제는 다음 규칙에 따라 프로세스를 관리한다
    - 1. 실행 대기 큐에서 대기 중인 프로세스를 하나 꺼낸다
    - 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣는다
    - 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행한다
        - 3-1. 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료된다
- 현재 실행 대기 큐에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities의 길이는 1 이상 100 이하이다
    - priorities의 원소는 1 이상 9 이하의 정수이다
    - priorities의 원소는 우선순위를 나타내며, 숫자가 클수록 우선순위가 높다
- 몇 번째로 실행되는지 알고 싶은 프로세스의 위치 location은 0 이상 (대기 큐에 있는 프로세스의 수 - 1) 이하이다
    - priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1, ... 과 같이 표현한다

Example:
- Input : priorities=[2, 1, 3, 2], location=2
- Output : 1

- Input : priorities=[1, 1, 9, 1, 1, 1], location=0
- Output: 5

Note:
실행 대기 큐를 구현하기 위해 ArrayDeque를, 가장 높은 우선순위를 빠르게 확인하기 위해 PriorityQueue 사용
큐에서 꺼낸 프로세스가 남아 있는 프로세스 중 우선순위가 가장 높은 것이 아니라면 큐에 다시 삽입
우선순위가 가장 높은 것이라면 힙에서도 같이 제거

 */

import java.util.PriorityQueue

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        val queue = ArrayDeque<Pair<Int, Int>>().apply {
            addAll(priorities.withIndex().map { (idx, pr) ->
                pr to idx
            })
        }
        val heap = PriorityQueue<Int>(compareByDescending { it }).apply { addAll(priorities.toList()) }

        var answer = 0
        while (queue.isNotEmpty()) {
            val (pr, idx) = queue.removeFirst()
            if (heap.peek() > pr) {
                queue.addLast(pr to idx)
            }
            else {
                heap.poll()
                answer++
                if (idx == location) return answer
            }
        }

        return 0
    }
}