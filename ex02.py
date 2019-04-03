import numpy as np

# numpy 배열의 연산
# broadCasting          ==> 어떤 값하나가 배열의 요소만큼 연산을 수행
# 1 + [1,2,3,4,5]

# vector Operation      ==> 두개의 배열의 인덱스가 같은 요소끼리 연산을 수행
# [1,2,3]+[4,5,6]       ==> 열의 크기가 같아야 해요


# a = np.array([1,2,3,4,5])
# b = a + 1           #배열의 요소에 각각 1을 더해 줍니다.  broadCasting
# print(b)


# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a + b                    vector Operation
# print(c)


# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[10,20,30],[40,50,60]])
#
# #a,b 두배열을 더하기 해 봅니다.
# #[[11,22,33],[44,55,66]]
# print(a+b)


# a = np.array([1,2,3,4,5,6])
# b = np.array([[10,20,30,],[40,50,60]])
# #a,b 두배열을 더하기 해 봅니다.
# #[[11,22,33],[44,55,66]]
#
# a = a.reshape(2,-1)
# print(a+b)


#broadCasting에 비교연산자를 사용하면  boolean Array을 얻어요
# a = np.array([1,3,0,7,9,5,6])
# b = a>5
# print(b)


#배열의 요소중에 원하는 인덱스의 요소만 추출할 수 있어요
#====> index Array
# a = np.array([1,3,0,7,9,5,6])
# #0번째 요소를 출력하고 싶어요
# print(a[0])
#
# #0번째하고 2번째요소하고 5번째 요소를 출력
# # print(a[0,2,5])   #a가 3차원배열인줄 알고 0번째 행의 2번째의 열, 5번째 면
# print(a[[0,2,5]])
#
#
# #0,2,5 요소만 출력하는 것을
# #boolean Array로 실험 해 봅니다.
# r = [True,False,True,False,False,True,False]
# print(a[r])

name = ['홍길동', '강감찬', '이순신', '유관순', '김유신']
score = [80,60,100,40,70]

#연습)
#60점이상이면 합격입니다.
#합격한 학생들의 이름을 출력해 봅니다.

name = np.array(name)
score = np.array(score)
print(name[score>=60])















