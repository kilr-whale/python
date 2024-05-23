for i in range(1, 51):
    with open(f"{i}주차.txt", "w", encoding="utf-8") as bogoseo:
        bogoseo.write(f"- {i} 주차 주간보고 -\n")
        bogoseo.write("부서 : \n")
        bogoseo.write("이름 : \n")
        bogoseo.write("업무 요약 : \n")