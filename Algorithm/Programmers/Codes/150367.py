"""

표현 가능한 이진트리 : https://school.programmers.co.kr/learn/courses/30/lessons/150367

정수가 주어졌을 때, 하나의 이진트리로 해당 수를 표현할 수 있는지 확인하는 문제
- 이진트리를 수로 표현하는 방법은 다음과 같다
    - 주어진 이진트리에 더미 노드를 추가하여 포화 이진트리로 만든다. 루트 노드는 그대로 유지한다
    - 포화 이진트리의 노드들을 가장 왼쪽부터 가장 오른쪽 노드까지 순서대로 살펴본다. 노드의 높이는 살펴보는 순서에 영향을 끼치지 않는다
    - 살펴본 노드가 더미 노드라면 0을, 더미 노드가 아니라면 1을 문자열에 추가한다
    - 문자열에 저장된 이진수를 십진수로 변환한다
- 이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브 트리의 노드들보다 오른쪽에 있으며, 자신의 오른쪽 자식이 루트인 서브 트리의 노드들보다 왼쪽에 있다고 가정한다
- 이진트리로 표현 가능하다면 1을, 표현할 수 없는 경우 0을 배열에 담아 리턴한다

Example:
- Input : numbers=[7, 42, 5]
- Output : [1, 1, 0]

- Input : numbers=[63, 111, 95]
- Output : [1, 1, 0]

Note:
주어진 숫자를 2진법으로 변환한 후, 포화 이진트리에 맞게 앞쪽에 0을 추가
dfs 방식으로 트리를 순회하며 조건에 맞는지 확인
서브 트리의 root가 0인데 자식 노드에 1이 있다면 잘못된 형식

"""

def solution(numbers):
    result = []

    def check_tree(tree):
        if tree == '1' or tree == '0':
            return True

        l = len(tree) // 2
        left, right, root = tree[:l], tree[l+1:], tree[l]

        if root == '0':
            if '1' in left or '1' in right:
                return False

        return check_tree(left) and check_tree(right)

    def get_full_tree(binary):
        l = len(binary)
        count, level = 1, 1
        while l > count:
            level *= 2
            count += level
        dummy = count - l
        return '0' * dummy + binary

    for number in numbers:
        binary = get_full_tree(bin(number)[2:])

        res = check_tree(binary)
        result.append(1 if res else 0)

    return result