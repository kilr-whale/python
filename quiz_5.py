from random import *

a = 0
for i in range(1, 51):
    Time = randint(5, 50)
    if Time <= 15 and Time >= 5 :
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, Time))
        a += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, Time))

print("총 탑승 승객 : {} 분".format(a))