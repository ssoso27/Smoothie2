def solution(participant, completion):
    answer = ''

    ht = {}
    for p in participant:
        if p not in ht.keys():
            ht[p] = 0
        ht[p] += 1

    for c in completion:
        ht[c] -= 1

    for h in ht:
        if ht[h] > 0:
            answer = h
            break

    return answer

ex = [
    (["leo", "kiki", "eden"], ["eden", "kiki"], "leo"),
    (["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"], "vinko"),
    (["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"], "mislav")
]
for p, c, r in ex:
    print(solution(p, c) == r)