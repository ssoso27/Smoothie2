def gugudan():
    lst = [str(i) + ' * ' + str(j) + ' = ' + str(i*j) for i in range(2, 9) for j in range(1, 9)]
    print(lst)

def gugudan_recursion(i, j):
    print(str(i) + ' * ' + str(j) + ' = ' + str(i*j))
    if i == 9 and j == 9:
        return

    if j == 9:
        gugudan_recursion(i+1, 1) # 외부
    else:
        gugudan_recursion(i, j+1) # 내부

gugudan()
gugudan_recursion(2, 1)