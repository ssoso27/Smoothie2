def solution(s):
    answer = []
    number_set = set()
    for st in sorted(s[2:-2].split("},{"), key=lambda x: len(x)):
        n = set(map(int, st.split(",")))
        answer.append(n.difference(number_set).pop())
        number_set.update(n)
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))