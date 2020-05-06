from collections import deque

pages = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
time = [0, 0]

chairs = deque()

q = deque()
q += pages
while q:
    top = q.popleft()

    # 자리가 남을 경우
    if len(chairs) < 3:
        chairs.append(top)
    # 자리가 남지 않을 경우
    else:
        # 중복이 있는 경우
        if top in chairs:
            time[1] += 1
        # 중복이 없는 경우
        else:
            time[0] += 1

        chairs.remove(top)
        chairs.append(top)

print(time[0] + "분 " + time[1] + "초")