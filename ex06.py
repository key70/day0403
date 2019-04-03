import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

path = "C:/Windows/Fonts/malgun.ttf"
rc('font', family=font_manager.FontProperties(fname=path).get_name())

qty = [10,20,10,30,50]
plt.bar(range(5),qty, 0.4)
plt.title("요일별 과일 판매량")
plt.show()


#차트에 한글이 안써져요
#rc('font', family=font_manager.FontProperties(fname=한글폰트파일의 경로).get_name())
#matplotlib의 rc와 font_manager가 필요해요
#from matplotlib import rc, font_manager


# 연습)
# 0.01에서 0.01씩 증가하여  2까지의 수들에 대한
# 지수값과 로그값을 하나의 화면에 차트를 그려 보세요.
# 두개의 차트를 가로로 나타내 봅니다.
# print(  np.exp(2) )
# print(  np.log(2) )

# x = np.arange(0.01, 2, 0.01)
# arr_exp = np.exp(x)
# arr_log = np.log(x)
#
# plt.subplot(121)
# plt.plot(x,arr_exp, 'r')
# plt.subplot(122)
# plt.plot(x,arr_log, 'b')
# plt.show()



# t1 = np.arange(0,5,0.1)
# t2 = np.arange(0,5, 0.02)
# plt.subplot(211)
# plt.plot(t1)
# plt.subplot(212)
# plt.plot(t2,"b")
# plt.show()

# plt.figure(1)
# plt.plot(t1, "ro")
#
# plt.figure(2)
# plt.plot(t2, "bo")
#
# plt.show()

# print(t1)
# print(t2)

#연습)
#x의 범위가 -10에서 10일때 x제곱값을 차트로 그려 주세요
# x = np.arange(-10,10)
# y = x ** 2
# print(x)
# print(y)
#
# plt.plot(x,y)
# plt.plot(x,y,"x")
# plt.show()


# height = np.array([170, 180, 160, 185, 167])
# weight = np.array([80,100,65,105,73])
#
# plt.plot(weight, height, "ro")
# plt.xlim(0,150)
# plt.ylim(100,200)
# plt.show()


# qty = np.array([60,100,30,40,150])
# plt.plot(qty)
# plt.show()
'''
            월   화       수    목      금
    딸기   1000  1100   1000      900   1500
    수박   80     80      100     50      40      
    포도   60     70      40      50      60
'''
# qty = np.array([[1000,1100,1000,900,1500],[80,80,100,50,40],[60,70,40,50,60]])

#수박에 대한 판매량의 정보를 차트로 나타내 봅니다.
# plt.plot(qty[1])
# plt.plot(qty[1], "ro")
# plt.show()

#  print(np.average(qty[1]))
# 수박에 대한 판매량에 대하여 평균판매량과의 차이를 차트로 나타내 봅니다.

# a =  np.abs(qty[1] - np.mean(qty[1]))
# # plt.plot(a, "bo")
# plt.plot(qty[1], a, "bo")
# plt.ylim(0,100)
# # plt.xlim(0,100)
# plt.show()










