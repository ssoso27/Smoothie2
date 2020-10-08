animals = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']

def solutuion(animals, n):
    chairs = [] * n
    answer = 0
    for animal in animals:
        if len(chairs) < 3:
            # 페이지 hit
            if animal in chairs:
                chairs.append(chairs.pop(0))
                answer += 1
            else: # hit가 일어나지 않은 경우
                chairs.append(animal)
                answer += 60
        else:
            # 페이지 hit
            if animal in chairs:
                chairs.append(chairs.pop(0))
                answer += 1
            else: # hit가 일어나지 않은 경우
                chairs.pop(0)
                chairs.append(animal)
                answer += 60

    return answer


print(solutuion(animals, 3))