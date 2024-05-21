import random
x = random.randint(1,20)

count = 4
while count > 0 :
    y = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(count)))
    count -= 1

    if count == 0:
        print("아쉽습니다. 정답은 {}였습니다.".format(x))
        break

    if x > y :
        print("Up")
    elif x < y :
        print("Down")
    elif x == y :
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(4-count))
        break

