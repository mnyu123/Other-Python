# BMI = 몸무게(kg)/키(m)의 제곱 BMI 측정 프로그램
print("BMI 측정 프로그램")
KG = input("몸무게 입력:")
CM = input("키 입력:")
REALCM = float(CM)/100
BMI = float(KG)/float(REALCM**2)
print("BMI는 %.1lf 입니다." %(BMI))
#빽
