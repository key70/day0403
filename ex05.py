import numpy as np
'''
            월   화       수    목      금
    딸기   1000  1100   1000      900   1500
    수박   80     80      100     50      40      
    포도   60     70      40      50      60
'''

qty = np.array([[1000,1100,1000,900,1500],[80,80,100,50,40],[60,70,40,50,60]])
print(qty)
print(np.max(qty))
print(np.max(qty, axis=0))
print(np.max(qty, axis=1))


# print(np.sum(qty))
# print(np.sum(qty,axis=0))
# print(np.sum(qty,axis=1))


# qty = np.array([200,1000,10,20,30,1000])
# r = np.sum(qty)
# r2 = np.max(qty)
# print(r)
# print(r2)







# item = ["사과","바나나","수박", "체리", "복숭아","딸기"]
# qty = [200,1000,10,20,30,1000]
#
# #연습)
# #판매량이 높은 순으로 과일명을 출력
# arr_item = np.array(item)
# arr_qty = np.array(qty)
#
# # n = np.argsort(arr_qty)[::-1]
# # print(arr_item[n])
#
# # n = np.argmax(arr_qty)       #최대값이 2개 이상일때는 첫번째 인덱스만 반환해요
# # print(arr_item[n])
#
#
# n = np.argwhere( arr_qty == np.amax(arr_qty)  )
# r = arr_item[n]
# r = r.reshape( r.size  )
# print(r)
# # print(arr_item[n])
# # print(arr_item[n].flatten())





# a = [7,6,1,5,3]
# #  2 4 3 1 0
# arr = np.array(a)
# # 정렬했을때 와야할 데이터의 순서를 반환하는 함수
# # 몇번째 요소부터 먼저 와야 하니?        ==> argsort
#
# idx = np.argsort(arr)
# print(idx)
# print(arr[idx])



# a = [7,6,1,5,3]
# arr = np.array(a)
# arr.sort()
# print(arr)
#
#





# 연습)
# 0으로 채워진 5*5 배열을 만들고 대각선으로 1로 채우세요
# a = np.zeros([5,5], dtype="int32")
# a[[0,1,2,3,4] , [0,1,2,3,4] ] = 1
# print(a)

# a = np.eye(5,5, dtype="int32")
# print(a)