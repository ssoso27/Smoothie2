def solution(k, room_number):
    answer = []
    checked = [False for _ in range(k+1)]
    checked[0] = True
    # nexts = {}
    # for i in range(1, k):
    #     nexts[i] = i+1
    # nexts[k] = k
    nexts = [i+1 for i in range(k+1)]
    nexts[0] = -1
    nexts[k] = k

    for room in room_number:
        select_room = room
        if checked[room]:
            # 다음 방 찾기
            select_room = nexts[room]

        # 방 배정해주기
        checked[select_room] = True
        answer.append(select_room)

        # next 방 합치기
        for r in range(1, len(nexts)):
            if nexts[r] == select_room:
                nexts[r] = nexts[select_room]

    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))