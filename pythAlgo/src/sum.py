def sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

def sum_recursion(lst):
    if len(lst) == 1:
        return lst.pop()
    return lst.pop() + sum_recursion(lst)

lst = [3, 5, 4, 6]
print(sum(lst))
print(sum_recursion(lst))