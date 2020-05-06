prime_number = []
result = set()


def make_prime_number(l):
    global prime_number
    N = 10 ** l
    prime_number = [True for _ in range(N)]
    prime_number[0] = False
    prime_number[1] = False

    for i in range(2, int(N**0.5)+1):
        if prime_number[i]:
            m = 2
            while True:
                if i*m >= N:
                    break
                prime_number[i*m] = False
                m += 1

    return prime_number


def is_prime_number(num):
    return prime_number[num]


def permutation(idx, selected, maken, numbers):
    if maken != "" and is_prime_number(int(maken)):
        result.add(int(maken))

    if idx == len(numbers):
        return

    for i in range(len(numbers)):
        if not selected[i]:
            maken += numbers[i]
            selected[i] = True

            permutation(idx+1, selected, maken, numbers)

            selected[i] = False
            maken = maken[:-1]


def solution(numbers):
    global result
    result = set()
    make_prime_number(len(numbers))

    selected = [False for _ in range(len(numbers))]
    permutation(0, selected, "", numbers)
    return len(result)


ex = [
    ("17", 3),
    ("011", 2)
]
for n, r in ex:
    print(solution(n) == r)