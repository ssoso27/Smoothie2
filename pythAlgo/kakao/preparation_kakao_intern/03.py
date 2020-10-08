WAITING = 14000605
days_of_month = [0] + [2**(11-m) for m in range(1, 11)]
board_of_minutes = [25, 15, 15, 15, 15, 15]
board_of_hour = sum(board_of_minutes)
board_of_day = board_of_hour * 12

year, month, day, hour, minutes = 2000, 1, 1, 9, 0

# 기다려야 하는 날짜 세기
waiting_days = (WAITING+1) // board_of_day
print("기다려야 하는 날짜 수 : " + str(waiting_days) + "일, " + str((WAITING+1) % board_of_day) + "분")

# 기다려야 하는 연도 세기
print("기다려야 하는 연도 : " + str(waiting_days//sum(days_of_month)) + "년, " + str(waiting_days%sum(days_of_month)) + "일")
m = 1
while m < len(days_of_month):
    if waiting_days >= days_of_month[m]:
        waiting_days -= days_of_month[m]
    else:
        break

print(m, waiting_days)