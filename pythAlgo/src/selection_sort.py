def selection_sort(lst):
    sorted_lst = []
    for i in range(len(lst)):
        min_idx = find_min_index(lst)
        sorted_lst.append(lst.pop(min_idx))
    return sorted_lst

def find_min_index(lst):
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[min_idx] > lst[i]:
            min_idx = i
    return min_idx

lst = [5, 4, 7, 6, 3, 2, 8, 1]
print( selection_sort(lst) )