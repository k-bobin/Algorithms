from collections import deque 
def solution(bridge_length, weight, truck_weights):
    answer = 0
    completed = []
    on_bridge = deque([0] * bridge_length)
    current_weight = sum(on_bridge)
    
    while len(truck_weights) :
        if current_weight - on_bridge[0] + truck_weights[0] <= weight:
            temp= truck_weights.pop(0)
            on_bridge.append(temp)
            current_weight += temp
            current_weight -= on_bridge.popleft()
            answer += 1 
        else:
            on_bridge.append(0)
            current_weight -= on_bridge.popleft()
            answer += 1 
            
    return answer + bridge_length
