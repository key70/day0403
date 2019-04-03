import numpy as np

#np.zeros       배열의 요소를 0으로 채워주세요
#np.ones        배열의 요소를 1로 채워주세요
#np.full        배열의 요소를 특정값으로 채워주세요


# a = np.zeros(10, dtype="int32")
# b = np.ones(5, dtype=np.int32)
# c = np.full(7,100)
#
# print(a)
# print(b)
# print(c)

# a = np.zeros([2,3], dtype="int32")
# b = np.ones([5,5],dtype="int32")
# c = np.full([5,5],100)
#
# print(a)
# print(b)
# print(c)


#연속된 데이터를 갖는 numpy 배열 생성
#np.arange
# a=np.arange(10)
# print(a)
#
# b = np.arange(1,11)
# print(b)
#
# c = np.arange(1,11,2)
# print(c)
#
# d = np.arange(10,-10,-1)
# print(d)


#파이썬배열 ==> numpy 배열         np.array
#numpy배열 ==> 파이썬 배열         list

# a = [1,2,3,4,5]
# b = np.array(a)
# print(a)
# print(b)
# print(a[2])
# print(b[2])

# a = np.arange(10,-10,-1)
# b = list(a)
# print(a)
# print(b)
#
# print(type(a))
# print(type(b))



#배열의 차수, 모양(몇행 몇열인지), 요소의 자료형
#ndim           shape                 dtype
# a = np.array([1,2,3,4,5])
# b = np.array([10.5, 2.7, 3.5])
# c = np.array([[1,2,3],[4,5,6]])
#
# print(a)
# print(b)
#
# #배열의 자료형        type ==> 배열자체가 numpy배열인지, python배열인지
# print(type(a))
# print(type(b))
#
# #배열의 요소의 자료형
# print(a.dtype)          #int32
# print(b.dtype)          #float64
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
#
# print(a.shape)
# print(b.shape)
# print(c.shape)


#numpy배열의 차원을 변경        ==> reshape

# a = np.array([1,2,3,4,5,6])
# b = a.reshape([2,3])
# print(a)
# print(b)


#차원을 변경할때 행이나 열중에 하나를 생략  -1
# a = np.array([1,2,3,4,5,6])
# # b = a.reshape([2,-1])
# b = a.reshape([-1,3])
# print(a)
# print(b)


# 2차원배열을 1차원 배열로 만들때는
# 내가 직접 데이터의수를 파악하기 보다는
# shape을 통해 행 * 열 만큼의 배열을 생성하도록 합니다.
# size  ==> 배열의 요소의 수를 알 수 있어요!
# 2차원에서 1차원 배열로 차원을 바꿀때   알아서 해줘  -1
a =  np.array([[1,2,3],[4,5,6]])
# print(a.size)
# print(len(a))
# print(len(a[0]))
# b = a.reshape(6)
# row, col = a.shape
# b = a.reshape( a.size )
# b = a.reshape( row*col )
# # b = a.reshape( len(a) * len(a[0])  )
b = a.reshape(-1)
print(a)
print(b)




































