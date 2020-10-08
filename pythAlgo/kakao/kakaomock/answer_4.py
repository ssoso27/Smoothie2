def find_blank_room(room, parents, checked):
    while checked[room]:
        room = parents[room]
    return room


def solution(k, room_number):
    answer = []

    # 부모 초기화
    parents = {}

    # 이미 찼는지 여부
    checked = [False for _ in range(k+1)]
    checked[0] = True

    for room in room_number:
        # 아직 부모 해시테이블이 만들어지지 않았으면
        if room not in parents.keys():
            parents[room] = room + 1

        # 알맞은 빈 방 찾기
        target_room = find_blank_room(room, parents, checked)

        # 방 채우고
        checked[target_room] = True
        answer.append(target_room)

        # 부모 합치기
        if target_room not in parents.keys():
            parents[target_room] = target_room + 1

        for k in parents.keys():
            # 방금 채워진 방을 부모로 갖고 있다면, 부모 교체
            if parents[k] == target_room:
                parents[k] = parents[target_room]

    return answer

