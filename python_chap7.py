#numpy 고속 처리 경험
import numpy as np
# import time
# from numpy.random import rand

# N = 150

# matA = np.array(rand(N, N))
# matB = np.array(rand(N, N))
# matC = np.array([[0] * N for _ in range(N)])
# start = time.time 

# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             matC[i][j] = matA[i][k] * matB[k][j]
# print("파이썬 기능만으로 계산한 결과: %.2f[sec]" % float(time.time() - start))

# start = time.time()
# matC = np.dot(matA, matB)

# print("Numpy를 사용하여 계산한 결과:  %.2f[sec]" % float(time.time() - start))

#1차원 배열의 계산
#numpy를 사용하지 않고
# storages = [1,2,3,4]
# new_storages = []
# for n in storages:
#     n += n
#     new_storages.append(n)
# print(new_storages)
# #numpy 사용
# import numpy as np
# storages = np.array([1,2,3,4])
# storages += storages
# print(storages)

# import numpy as np
# arr = np.arange(10)
# print(arr)
# print(arr[3:6])
# arr[3:6] = 24
# print(arr)

# arr = np.array([2,4,6,7])
# print(arr[np.array([True, True, True, False])])

# arr = np.array([2,4,6,7])
# print(arr[np.array([True, True, True, False])])

# print(arr[arr % 3 == 1])

# arr2 = np.array([2,3,4,5,6,7])
# print(arr2 % 2 == 0)
# print(arr[arr % 2 == 0])

# arr = np.array([4, -9, 16, -4, 20])
# print(arr)
# arr_abs = np.abs(arr)
# print(arr_abs)
# print(np.exp(arr_abs))
# print(np.sqrt(arr_abs))

# #집합 함수
# arr1 = [2,5,7,9,5,2]
# arr2 = [2,5,8,3,1]

# new_arr1 = np.unique(arr1)
# print(new_arr1)

# print(np.union1d(new_arr1, arr2)) #합집합
# print(np.intersect1d(new_arr1, arr2)) # 교집합
# print(np.setdiff1d(new_arr1, arr2)) #차집합

#난수
# import numpy as np
# from numpy.random import randint
# arr1 = randint(0,11, (5,2))
# arr2 = np.random.rand(3)
# print(arr2)

#2차원배열
# import numpy as np
# arr = np.array([[1,2,3,4], [5,6,7,8]])
# print(arr)

# print(arr.shape)
# print(arr.reshape(4,2))

#인덱스 참조와 슬라이스
# import numpy as np
# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr)
# print(arr[0,2])
# print(arr[1:, :2])

# import numpy as np
# arr = np.array([[1,2,3], [4,5,12], [15,20,22])
# print(arr.sum(axis=1))

# #팬시 인덱스 참조
# import as np
# arr = np.arange(25).reshape(5,5)
# print(arr[[1,3,0]])

#전치 행렬
# import numpy as np
# arr = np.arange(10).reshape(2,5)
# print(arr.T)

#정렬
# arr = np.array([15, 30, 5])
# arr.argsort()
# array([2,0,1], dtype= int64)

# import numpy as np
# arr = np.array([[8,4,2], [3,5,1]])
# print(arr.argsort())
# print(np.sort(arr))

# arr.sort(1)
# print(arr)

# #행렬 계산
# import numpy as np
# arr = np.array(9).reshape(3,3)
# print(np.dot(arr, arr))
# vec = arr.reshape(9)
# print(np.linalg.norm(vec))

#통계함수
# import numpy as np
# arr = np.array(15).reshape(3,5)
# print(arr.mean(axis=0))
# print(arr.sum(axis=1))
# print(arr.min())
# print(arr.argmax(axis=0))

#문제 
import numpy as np
np.random.seed(100)
arr = np.random.randint(0, 31, (5, 3))
print(arr)
arr = arr.T
print(arr)
arr1 = arr[:, 1:4]
print(arr1)
arr1.sort(0)
print(arr1)
print(arr1.mean(axis=0))
