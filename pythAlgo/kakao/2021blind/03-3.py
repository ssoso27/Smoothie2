def solution(info, query):
    answer = [0 for _ in range(len(query))]
    people = [[0] for _ in range(len(info))]

    # 지원자 정보 저장
    for idx in range(len(info)):
        people[idx] = [n for n in info[idx].split(" ")]
        people[idx][4] = int(people[idx][4])

    # 질의
    for idx in range(len(query)):
        l, j, c, f, s = [n for n in query[idx].split(" ") if n != "and"]
        s = int(s)

        cnt = 0
        for p in people:
            if (l == "-" or l == p[0]) \
                and (j == "-" or j == p[1]) \
                and (c == "-" or c == p[2]) \
                and (f == "-" or f == p[3]) \
                and s <= p[4]:
                    cnt += 1

        answer[idx] = cnt

    return answer