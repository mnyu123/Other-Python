import numpy as np


c=np.random.randint(0,25,(5,5)) # 25까지 랜덤한 자연수 5x5 행렬로 생성

d=np.ravel(c) # 이차원 배열을 일차원 배열로 쫙 폈다

e=np.sort(d) # 일차원 배열 숫자 내림차순으로 정렬
print(e)

f=e.reshape(5,5) # 다시 정렬된 일차원 배열의 숫자를 이차원 배열로 재조립
print(f)

