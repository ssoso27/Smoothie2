def solution(v):
    xlist, ylist = [], []

    for (x, y) in v:
        if x in xlist:
            xlist.remove(x)
        else:
            xlist.append(x)

        if y in ylist:
            ylist.remove(y)
        else:
            ylist.append(y)

    return [xlist.pop(), ylist.pop()]


v = [[1, 4], [3, 4], [3, 10]]
result = [1, 10]
print(solution(v))