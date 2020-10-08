def solution(info, query):
    answer = []

    languages = {
        "cpp": [],
        "java": [],
        "python": [],
        "-": range(len(info))
    }

    jobs = {
        "backend": [],
        "frontend": [],
        "-": range(len(info))
    }

    careers = {
        "junior": [],
        "senior": [],
        "-": range(len(info))
    }

    foods = {
        "chicken": [],
        "pizza": [],
        "-": range(len(info))
    }

    scores = [0 for _ in range(len(info))]

    # 지원자 정보 저장
    for idx, row in enumerate(info):
        l, j, c, f, s = [n.strip() for n in row.split(" ")]
        languages[l].append(idx)
        jobs[j].append(idx)
        careers[c].append(idx)
        foods[f].append(idx)
        scores[idx] = int(s)

    # 질의
    for row in query:
        l, j, c, f, s = [n.strip() for n in row.split(" ") if n.strip() != "and"]
        s = int(s)

        cnt = 0
        for p in languages[l]:
            if p in jobs[j] and p in careers[c] and p in foods[f] and scores[p] >= s:
                cnt += 1

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = [1,1,1,1,2,4]
print(solution(info, query) == result)