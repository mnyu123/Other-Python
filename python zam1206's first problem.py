print("----------빽----------") # 떽!
 
import random # 무요 이것도 읽을꺼야?

binaryCost1 = random.randint(1,256) # 아저씨가 범위 안줘서 그냥 내가 정함
binaryCost2 = random.randint(1,256) # 2번 피연산자

print(binaryCost1) # 10진수 랜덤숫자가 잘 나오는지 테스트 
print(binaryCost2) # 두번째 자연수가 잘 나오나 테스트
print("----------------------")

realbinary1 = format(binaryCost1 , 'b') # 2진수 변환 함수 format
realbinary2 = format(binaryCost2 , 'b') 

realbinary1 = bin(binaryCost1) # 2진수로 바뀌였다.
realbinary2 = bin(binaryCost2)


print(realbinary1[2:]) # 앞에 ob는 떼고 출력해줌 정상적으로 이진수 출력
print(realbinary2[2:]) # 두번째 이진수
print("----------------------")


def plus(realbinary1,realbinary2):
    binaryplus = realbinary1 + realbinary2
    print(binaryplus[2:]) # 맨앞에 0b 지우는거임
    print(type(binaryplus))
    return binaryplus


plus(realbinary1,realbinary2)

def sub(realbinary1,realbinary2):
    realbinary2 # 2의보수 구현해야함

    # 2의 보수 구현한 값을 realbinaray1과 덧셈연산 해서
    # 이진수 뺄셈 구현해야함

def onebous(realbinary1,realbinary2):
    realbinary1 
    # 1의 보수에 1을 더하는 수식
    # 결과 반환