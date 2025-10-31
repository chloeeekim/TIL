"""

영어 끝말잇기 : https://school.programmers.co.kr/learn/courses/30/lessons/12981

1부터 n까지의 사람이 영어 끝말잇기를 할 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구하는 문제
- 영어 끝말잇기 규칙은 다음과 같다
    - 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말한다
    - 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작한다
    - 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 한다
    - 이전에 등장했던 단어는 사용할 수 없다
    - 한 글자인 단어는 인정되지 않는다
- 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수이다
- words는 끝말잇기에 사용된 단어들이 순서대로 들어있는 배열로, 길이는 n 이상 100 이하이다
    - words의 원소의 길이는 2 이상 50 이하이다
    - 모든 단어는 알파벳 소문자로만 이루어져 있다
    - 끝말잇기에 사용되는 단어의 뜻은 신경쓰지 않아도 된다
- [번호, 차례]의 형태로 리턴한다
    - 만약 주어진 단어들로 탈락자가 생기지 않는다면 [0, 0]을 리턴한다

Example:
- Input : n=3, words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
- Output : [3,3]
- 3번 사람이 세 번째 차례에 말한 tank가 중복

- Input : n=5, words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
- Output : [0,0]

- Input : n=2, words=["hello", "one", "even", "never", "now", "world", "draw"]
- Output : [1,3]
- 1번 사람이 세 번째 차례에 말한 now는 앞 단어의 마지막 문자(r)로 시작하지 않는다

Note:
used 배열을 두어 이미 사용되었는지 판별
한 글자인 단어는 인정되지 않는다고 하였는데, 주어지는 단어의 길이가 2 이상으로 제한되어 있으므로, 해당 조건은 신경쓰지 않는다

"""

def solution(n, words):
    used = [words[0]]
    last = words[0][-1]
    for i in range(1, len(words)):
        if words[i] in used or last != words[i][0]:
            return [i%n + 1, i//n + 1]
        last = words[i][-1]
        used.append(words[i])
    return [0, 0]