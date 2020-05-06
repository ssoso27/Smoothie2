from sys import stdin
input = stdin.readline

N = int(input())
skills = [[] for _ in range(N)]

for i in range(N):
    skills[i] = [i] + list(map(int, input().split(" ")))

sorted_skills = sorted(skills, key=lambda x: x[1])

attackable = [0 for _ in range(N)]
for i in range(1, N):
    idx, s, e = sorted_skills[i]
    for j in range(i):
        nidx, ns, ne = sorted_skills[j]
        if ns < s and ne > s:
            attackable[idx] += 1

for a in attackable:
    print(a)