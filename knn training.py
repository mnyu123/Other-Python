# 필요한 패키지를 불러옴
from cProfile import label
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# iris 데이터 셋을 불러오는 작업
iris = load_iris()
print(iris['feature_names']) # 특징
print(iris['data']) # 훈련 데이터
print(iris['target']) # 완성된 모델을 테스트할 데이터


x_train , x_test , y_train , y_test = \
    train_test_split(iris['data'],iris['target'],test_size = 0.2) 
    # 위의 줄 아마 훈련데이터와('데이터') 테스트데이터(타겟) test_size=0.2
    # 8:2로 나누는 작업일듯

# 분류를 하기 위해 knn모델을 불러와서 모델을 만들고 학습시킴
knn = KNeighborsClassifier(n_neighbors=6 , p=2 , metric='minkowski') 
# metric 저 부분 좀 다시 알아야 할듯
knn.fit(x_train,y_train) # 아마도 훈련 데이터를 저 metrics에다가 뿌리는 작업일듯

y_pred = knn.predict # y_pred에 knn알고리즘으로 예측한 결과 저장
accuracy = (y_test == y_pred).mean() # y_test데이터는 정답 결과 
# 그리고 y_pred는 AI가 KNN 알고리즘을 써서 만든 결과 얼마나 비슷한지 비교해서 숫자로 나타낸것일듯
print('테스트 데이터로 측정한 정확도 = %.2f' % accuracy) # 정확도 출력

# i를 바꿔보면서 정확도 측정 그림도 같이 출력해서 정확도 변화 확인
test_array=[]
train_array=[]
for i in range(1,50): # i가 1부터 49 까지
    # knn으로 train 데이터세트를 학습
    knn = KNeighborsClassifier(n_neighbors=i , p=2 , metric='minkowski')
    knn.fit(x_train,y_train)

    # test 세트의 feature에 대한 정확도
    y_pred = knn.predict(x_test)
    test_array.append((y_test == y_pred).sum() / len(y_pred))

    # train 세트의 feature에 대한 정확도
    y_pred = knn.predict(x_train)
    train_array.append((y_train == y_pred).sum() / len(y_pred))

# 시각화
plt.figure(figsize=(8,5))
plt.plot(test_array , label = "test data")
plt.plot(train_array , label = "train data")
plt.legend()
plt.xlabel("i")
plt.ylabel("Accuracy")
plt.show()
