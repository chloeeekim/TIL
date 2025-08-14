"""

비밀 코드 해독 : https://school.programmers.co.kr/learn/courses/30/lessons/388352

1부터 n까지 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드가 있을 때, m번의 시도 후 비밀 코드로 가능한 정수 조합의 개수를 구하는 문제
- 각 시도마다 서로 다른 5개의 정수를 입력하면, 몇 개가 비밀 코드에 포함되어 있는지 확인 가능하다
- 비밀 코드가 존재하지 않는 경우(답이 0인 경우)는 주어지지 않는다

Example:
- Input : n=10, q=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], ans=[2, 3, 4, 3, 3]
- Output : 3
- 가능한 정수 조합은 [3, 4, 7, 9, 10], [3, 5, 7, 8, 9], [3, 5, 7, 8, 10]으로 3가지

- Input : n=15, q=	[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], ans=[2, 1, 3, 0, 1]
- Output : 5
- 가능한 정수 조합은 [1, 2, 3, 5, 8], [1, 3, 5, 8, 12], [2, 4, 5, 8, 12], [2, 5, 8, 9, 10], [5, 8, 9, 10, 12]으로 5가지

Note:
ans가 5라면 비밀 코드와 일치하는 것이므로 가능한 정수 조합은 1가지
ans가 0이라면 비밀 코드와 일치하는 숫자가 하나도 없으므로, 해당 숫자들은 제외
가능한 모든 조합을 구성한 후 교집합을 통해 비밀 코드로 가능한지 확인

"""

def solution(n, q, ans):
    m = len(q)
    nums = [0 for _ in range(n + 1)]
    count = 0
    for i, match in enumerate(ans):
        if match == 5:
            return 1
        if match == 0:
            for no in q[i]:
                nums[no] = -1

    def make_list():
        lists = []
        filtered = [i for i in range(1, n + 1) if nums[i] != -1]
        len_f = len(filtered)

        for i in range(len_f):
            for j in range(i + 1, len_f):
                for k in range(j + 1, len_f):
                    for l in range(k + 1, len_f):
                        for m in range(l + 1, len_f):
                            lists.append([filtered[i], filtered[j], filtered[k], filtered[l], filtered[m]])
        return lists

    def check(l):
        for i in range(m):
            if len(set(l) & set(q[i])) != ans[i]:
                return False
        return True

    lists = make_list()
    for l in lists:
        if check(l):
            count += 1
    return count