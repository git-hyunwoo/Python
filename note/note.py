import numpy as np

# 1차원 배열 생성
array1 = np.array([1,2,3,4,5])

# 2차원 배열 생성
array2 = np.array([[1,2,3],[4,5,6]])

# 배열의 데이터 타입 지정
array3 = np.array([1,2,3], dtype = np.float64)


# 요소별 덧셈
result1 = array1 + 2
print(result1) # 출력 : [3 4 5 6 7]

# 요소별 곱셈
result2 = array1 * 3
print(result2) # 출력 : [3 6 9 12 15]

# 배열 간 덧셈
result3 = array1 + array1
print(result3) # 출력 : [2 4 6 8 10]

# 행렬 곱셈
result4 = np.dot(array1, array1)
print(result4)




