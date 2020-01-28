from collections import deque

# 이 사람이 망고 판매자인지 확인하는 함수
def is_mango_seller(name):
    return name == "thom"

# 1. 방향 그래프 생성
graph = {}
graph["you"] = ["alice", "bob", "claire"] # you -> alice / you -> bob / you -> claire
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 2. 양방향 큐 생성
searched = [] # 이미 검색한 사람
search_queue = deque()
# 3. 큐에 "you"의 지인 추가 (1차 지인)
search_queue += graph["you"]

while search_queue: # 큐가 비어있지 않은 동안
    # 4. 큐에서 한 사람 (첫 사람) 을 꺼낸다.
    target = search_queue.popleft()
    if target not in searched: # 이 사람이 탐색한 사람이 아니라면
        searched.append(target) # 이 사람을 탐색했다고 추가
        if is_mango_seller(target): # 5-1. 이 사람이 망고 상인이면
           print(target + " is mango seller! ")
           break # 탐색 종료
        else: # 5-2. 이 사람이 망고 상인이 아니면
            # 큐에 이 사람의 지인 추가
            search_queue += graph[target]

