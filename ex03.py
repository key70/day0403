import numpy as np

# a = [0,1,2,3,4,5,6,7,8,9]
# print(a[0])
# print(a[1])
# print(a[0:3])
# print(a[-1])
# print(a[-2])
# print(a[3:])
# print(a[:3])           #시작하는 index는 포함이 되지만, 끝나는 index는 포함되지 않아요
# print(a[[0,3,4]])      #파이썬 배열에는 index Array를 사용할 수 없어요!
# print(a[[False,True,False,True,False,False,False,False,False,False]])     #boolean Array도 파이썬 배열에는 적용할 수 없어요
# print(a[0:10:2])
# print(a[::2])
# print(a[::-1])
#
# b = np.array(a)
# print(b[0])
# print(b[1])
# print(b[0:3])
# print(b[-1])
# print(b[-2])
# print(b[3:])
# print(b[:3])
# print(b[[0,3,4]])
# print(b[[False,True,False,True,False,False,False,False,False,False]])
# print(b[0:10:2])
# print(b[::2])
# print(b[::-1])


#2차원 배열에서의 slicing
a = [[1, 2,  3, 4, 5, 6],
     [7, 8,  9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24]]
b = np.array(a)

#연습) 배열중에 9, 12, 14, 17, 20, 22, 23이 있는 요소의
# arrayIndex를 만들고, fancy Indexing사용하여 뽑아 봅니다.
rows = [1,1,2,2,3,3,3]
cols = [2,5,1,4,1,3,4]

print(b[ rows , cols])










# print(b[1,])
# print(b[1:3, ])
# print(b[[1,2], ])

#연습)
#모든행에 대하여 1열부터, 4열까지의 데이터를 출력해 봅니다.
# print(b[:,1:5 ])


#연습)
#모든행에 대하여 1열, 3, 5열의 데이터를 출력해 봅니다.
# print(b)
# print(b[:, [1,3,5]])


#연습)
#짝수행만 모두 출력해 봅니다.
# print(b)
# print(b[1::2])
# print(b[1::2,:])


#연습)
#짝수행에 대하여 1열부터 4열까지의 데이터를 출력해 봅니다.

# print(b)
# print(b[::2, 1:5])

# c = np.array([1,2,3,4,5,6,7,8,9,10])

# print(a[1,2])           #파이썬 array는 fancy Indexing을 사용할 수 없어요
# print(b[1,2])
#fancy indexing의 형식     배열명[행 , 열]
#                          배열명[[index array]  , [index array]  ]
#                          배열명[[boolean array]  , [boolean array]  ]










# print(a[1][2])        값 하나를 뽑아 올때는 이와 같은 표현이 가능해요
# print(a[:][1])        범위를 주어서 slicing을 할때는 이렇게 표현할 수 없어요
#                           ===> fancy indexing을 사용해야 해요.

# print(c[:])
# print(a[:])
# print(b[:])


# print(c[:4])
# print(a[:4])
# print(b[:4])
# print(c[1:4])
# print(a[1:4])
# print(b[1:4])

# print(c[1])
# print(a[1])
# print(b[1])


# print(a[1][2])
# print(b[1][2])
# print(c[8])


















