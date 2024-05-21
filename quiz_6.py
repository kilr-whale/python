def std_weight(height, gender):
    if (gender == "남자") :
        return round(height/100 * height/100 * 22, 2)
    elif (gender == "여자") :
        return round(height/100 * height/100 * 21, 2)
    else :
        print("성별을 다시 입력하여 주세요.")
        exit(0)

height, gender = input("키와 성별을 입력하세요. : ").split(' ')
height = int(height)
gender = str(gender)

weight = std_weight(height, gender)
print("키 {0} {1}의 표준 체중은 {2}입니다.".format(height, gender, weight))


