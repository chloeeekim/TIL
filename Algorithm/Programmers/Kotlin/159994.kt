/*

카드 뭉치 : https://school.programmers.co.kr/learn/courses/30/lessons/159994

영어 단어가 적힌 카드 뭉치 두 개와 만들고자 하는 단어 배열이 주어졌을 때, 가능한 지 여부를 확인하는 문제
- 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 단어 배열을 만든다
    - 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용한다
    - 한 번 사용한 카드는 다시 사용할 수 없다
    - 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다
    - 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없다
- 카드 뭉치 cards1, cards2의 길이는 1 이상 10 이하이다
    - cards1[i], cards2[i]의 길이는 1 이상 10 이하이다
    - cards1과 cards2에는 서로 다른 단어만 존재한다
- 원하는 단어 배열 goal의 길이는 2 이상 cards1의 길이 + cards2의 길이 이하이다
    - goal[i]의 길이는 1 이상 10 이하이다
    - goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있다
- cards1, cards2, goal의 문자열들은 모두 알파벳 소문자로만 이루어져 있다
- 만들 수 있는 경우 "Yes"를, 만들 수 없는 경우 "No"를 리턴한다

Example:
- Input : cards1=["i", "drink", "water"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "Yes"

- Input : cards1=["i", "water", "drink"], cards2=["want", "to"], goal=["i", "want", "to", "drink", "water"]
- Output : "No"

Note:
cards1과 cards2의 현재 카드를 가리키는 인덱스를 각각 설정하여 확인
cards1[idx1]과 cards2[idx2] 둘 다 일치하지 않는 경우, 만들 수 없으므로 No를 리턴

 */

class Solution {
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        var idx1 = 0
        var idx2 = 0

        val isPossible = goal.all { word ->
            when {
                idx1 < cards1.size && cards1[idx1] == word -> {
                    idx1++
                    true
                }
                idx2 < cards2.size && cards2[idx2] == word -> {
                    idx2++
                    true
                }
                else -> false
            }
        }

        return if (isPossible) "Yes" else "No"
    }
}