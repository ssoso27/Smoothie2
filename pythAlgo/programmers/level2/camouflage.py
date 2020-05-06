def solution(clothes):
    answer = 1
    closet = {}
    for c, t in clothes:
        if t not in closet.keys():
            closet[t] = []
        closet[t].append(c)

    for type in closet.keys():
        answer *= len(closet[type])+1

    return answer-1


ex = [
    ([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], 5),
    ([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]], 3)
]
for c, r in ex:
    print(solution(c) == r)