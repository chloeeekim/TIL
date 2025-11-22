/*

순위 : https://school.programmers.co.kr/learn/courses/30/lessons/49191

선수들의 경기 결과 일부가 주어졌을 때, 정확하게 순위를 매길 수 있는 선수의 수를 구하는 문제
- 대회는 다음과 같이 진행된다
    - 각각 1번부터 n번까지 번호를 받은 n명의 선수가 있다
    - 경기는 1대1 방식으로 진행된다
    - 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이긴다
- 선수의 수 n은 1 이상 100 이하이다
- 경기 결과를 담은 2차원 배열 results의 길이는 1 이상 4,500 이하이다
    - results의 원소는 [A, B] 형식으로, A 선수가 B 선수를 이겼다는 의미이다
- 모든 경기 결과에는 모순이 없다

Example:
- Input : n=5, results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
- Output : 2

Note:
각 선수들의 경기 결과를 2차원 배열로 구성하여 a가 b에게 이긴 경우, arr[a][b]를 1로, 진 경우 -1로 저장 (자기 자신은 0)
만약 a가 mid를 이기고, mid가 b를 이긴다면 a도 b를 이기는 것이 명확해진다
반대로 a가 mid에게 지고, mid가 b에게 진다면 a도 b에게 지는 것이 명확해진다
최종적으로 모든 선수와의 결과를 알 수 있다면 해당 선수의 순위를 알 수 있다

 */

class Solution {
    fun solution(n: Int, results: Array<IntArray>): Int {
        val arr = Array(n + 1) { Array<Int?>(n + 1) { null } }

        for ((a, b) in results) {
            arr[a][a] = 0
            arr[b][b] = 0
            arr[a][b] = 1
            arr[b][a] = -1
        }

        for (mid in 1 .. n) {
            for (a in 1 .. n) {
                for (b in 1 .. n) {
                    if (arr[a][mid] == 1 && arr[mid][b] == 1) {
                        arr[a][b] = 1
                        arr[b][a] = -1
                    }
                    else if (arr[a][mid] == -1 && arr[mid][b] == -1) {
                        arr[a][b] = -1
                        arr[b][a] = 1
                    }
                }
            }
        }

        return arr.count { row ->
            row.filter{ it != null }.size == n
        }
    }
}