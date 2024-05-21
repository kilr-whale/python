from random import *

users = set(range(1, 21))


print("-- 당첨자 발표 --")
print("치킨 당첨자 : " + str(sample(users, 1)))
print("커피 당첨자 : " + str(sample(users, 3)))
print("-- 축하합니다 --")