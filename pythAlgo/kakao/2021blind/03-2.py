def solution(info, query):
    answer = []
    people = []

    # 지원자 정보 저장
    for row in info:
        people.append([n.strip() for n in row.split(" ")])
        people[-1][4] = int(people[-1][4])

    # 질의
    for row in query:
        l, j, c, f, s = [n.strip() for n in row.split(" ") if n.strip() != "and"]
        s = int(s)

        cnt = 0
        for idx, p in enumerate(people):
            if (l == "-" or l == p[0]) \
                and (j == "-" or j == p[1]) \
                and (c == "-" or c == p[2]) \
                and (f == "-" or f == p[3]) \
                and s <= p[4]:
                    cnt += 1

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = [1,1,1,1,2,4]
print(solution(info, query) == result)