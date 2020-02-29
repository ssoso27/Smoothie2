states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # 아직 방송이 되지 않은 주 집합

stations = {} # k:방송국명, v:커버링지역집합
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"]= set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set() # 방문할 방송국 집합

while states_needed: # 방송 안 된 주가 있는 동안
    # (아직 방송이 되지 않은 주 중) 가장 많은 주를 커버하고 있는 방송국 고르기
    best_station = None # 골라진 방송국
    states_covered = set() # 골라진 방송국이 커버하는 state의 집합
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 교집합 - 새로이 방송 될 주
        if len(covered) > len(states_covered): # 방송될주가 가장 많은 방송국 찾기
            best_station = station
            states_covered = covered

    # 방문할 방송국 집합에 골라진 방송국 추가
    final_stations.add(best_station)

    states_needed = states_needed - states_covered # 방송안된주집합 - 방송된주집합

print(final_stations)