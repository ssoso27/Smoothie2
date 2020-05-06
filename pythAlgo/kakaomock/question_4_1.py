parents = {}


def find_next_room(room):
    if parents[room] != room:
        parents[room] = find_next_room(parents[room])

    return parents[room]


def solution(k, room_number):
    answer = []

    for i in range(1, k+1):
        parents[i] = i

    for room in room_number:
        select_room = find_next_room(room)
        answer.append(select_room)
        if select_room < k:
            parents[select_room] = parents[select_room+1]

    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))