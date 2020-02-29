# https://www.acmicpc.net/problem/2798
n, m = map(int, input().split(" "))
cards = [int(i) for i in input().split(" ")]
cards.sort(reverse=True)

sum = 0
answer = 0
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             sum = cards[i] + cards[j] + cards[k]
#             #print(str(cards[i]) + " " + str(cards[j]) + " " + str(cards[k]) + " -> " + str(sum))
#             if sum <= m and sum > answer:
#                 answer = sum
#
# print(answer)
#
# def new_blackjack(i, j, k):
#     sum = cards[i] + cards[j] + cards[k]
#     #print(str(cards[i]) + " " + str(cards[j]) + " " + str(cards[k]) + " -> " + str(sum))
#     if sum <= m: # 조건에 부합하면 return
#         return sum # i, j, k+1 ... 과 i, j+1, k ... 은 전부 sum보다 작음
#
#     # 다음 재귀 단계
#     if k < n-1:
#         return new_blackjack(i, j, k+1)
#     elif k == n-1 and j < n-2:
#         return new_blackjack(i, j+1, j+2)
#     elif k == n-1 and j == n-2 and i < n-3:
#         return new_blackjack(i+1, i+2, i+3)
#     # 기본 단계
#     elif i == n-3 and j == n-2 and k == n-1: # 마지막 케이스에 도달
#         return -1
#
# print(new_blackjack(0, 1, 2))

def new_blackjack2(sum, idx, cnt):
    sum = sum + cards[idx]

    # 기본 단계
    if cnt == 3: # 카운트가 3일 경우
        if sum < m:
            return sum
        else:
            return -1
    if sum > m: # 이미 초과했을 경우
        return -1
    if idx >= n-1: # out of index
        return -1

    return max(new_blackjack2(sum, idx+1, cnt+1), new_blackjack2(sum, idx+2, cnt+1))

print(new_blackjack2(0, 0, 1))