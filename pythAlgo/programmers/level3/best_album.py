def solution(genres, plays):
    answer = []

    list_by_genre = {}
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        if g not in list_by_genre.keys():
            list_by_genre[g] = [0]
        list_by_genre[g][0] += p
        list_by_genre[g].append((i, p))

    much_play_genre = sorted(list_by_genre.keys(), key=lambda x: list_by_genre[x][0], reverse=True)[:2]

    for g in much_play_genre:
        lst = sorted(list_by_genre[g][1:], key=lambda x: x[1], reverse=True)
        if len(lst) < 2:
            answer.append(lst[0][0])
        else:
            for i in range(2):
                answer.append(lst[i][0])

    return answer

ex = [
    (["classic", "pop", "classic", "classic", "pop", "rock"], [500, 600, 150, 800, 2500, 5000], [5, 4, 1]),
    (["classic", "pop", "classic", "classic", "pop", "rock", "pop"], [500, 600, 150, 800, 2500, 5000, 5000], [6, 4, 5]),
    (["classic", "pop", "classic", "classic", "pop", "rock", "rock"], [500, 600, 150, 800, 2500, 5000, 5000], [5, 6, 4, 1]),
    (["classic", "pop", "classic", "classic", "pop", "rock", "rock", "rock"], [500, 600, 150, 800, 2500, 5000, 5000, 5000], [5, 6, 4, 1]),
    (["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 1, 3, 0]),
    (["classic", "pop"], [500, 600], [1, 0]),
    (["pop", "classic", "pop"], [600, 500, 600], [0, 2, 1]),
    (["pop"], [100], [0])
]
for g, p, r in ex:
    a = solution(g, p)
    print(a, a == r)