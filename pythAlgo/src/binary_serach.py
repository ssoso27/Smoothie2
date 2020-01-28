def binary_search(lst, item):
    print("binary search")
    low = 0
    high = len(lst) - 1

    while(low < high):
        idx = (high + low) // 2
        print("target : " + str(lst[idx]))
        if lst[idx] == item:
            print("search success")
            return idx
        if lst[idx] > item:
            print("down")
            high = idx - 1
        elif lst[idx] < item:
            print("up")
            low = idx + 1

    return None

lst = range(1, 10)
item = 15
print( binary_search(lst, item) )