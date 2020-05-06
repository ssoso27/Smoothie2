from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting_queue, running_queue = deque(), deque()

    waiting_queue.extend(truck_weights)
    running_queue.extend([0 for _ in range(bridge_length)])

    while waiting_queue:
        truck = waiting_queue.popleft()
        # 지금 트럭이 다리에 올라갈 수 있으면
        if sum(running_queue) + truck <= weight:
            pass
        else: # 무게 초과면
            pass

    return answer

ex = [
    (2, 10, [7,4,5,6], 8),
    (100, 100, [10], 101),
    (100, 100, [10,10,10,10,10,10,10,10,10,10], 110)
]