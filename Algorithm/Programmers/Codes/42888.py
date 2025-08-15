"""

오픈채팅방 : https://school.programmers.co.kr/learn/courses/30/lessons/42888

사용자의 채팅방 출입 및 닉네임 변경 기록이 주어졌을 때, 방을 개설한 사람이 최종적으로 보게 되는 메시지를 구하는 문제
- 채팅방에 누군가 들어오면 "[닉네임]님이 들어왔습니다." 메시지가 출력된다
- 채팅방에 누군가 나가면 "[닉네임]님이 나갔습니다." 메시지가 출력된다
- 누군가 닉네임을 변경하면 기존 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다
- record의 원소는 다음과 같은 형태를 지닌다
    - 채팅방에 입장 시: "Enter [유저 아이디] [닉네임]"
    - 채팅방에서 퇴장 시: "Leave [유저 아이디]"
    - 닉네임 변경 시: "Change [유저 아이디] [닉네임]"
    - 모든 유저는 [유저 아이디]로 구분한다
    - 각 단어는 공백으로 구분되며, 알파벳 대소문자 및 숫자로만 이루어져 있다
    - 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다
    - 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못된 입력은 주어지지 않는다

Example:
- Input : record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
- Output : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

Note:
최종적으로 변경된 닉네임을 확인하기 위해 defaultdict 사용
닉네임 변경에 대해서는 결과 메시지를 출력하지 않으므로, 채팅방 입장 및 퇴장에 대해서만 messages에 추가

"""

from collections import defaultdict

def solution(record):
    user_nickname = defaultdict()
    messages = []
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for r in record:
        rsp = r.split()
        if rsp[0] == 'Enter':
            user_nickname[rsp[1]] = rsp[2]
            messages.append([rsp[0], rsp[1]])
        elif rsp[0] == 'Change':
            user_nickname[rsp[1]] = rsp[2]
        elif rsp[0] == 'Leave':
            messages.append([rsp[0], rsp[1]])
    result = [user_nickname[uid] + message[case] for case, uid in messages]
    return result