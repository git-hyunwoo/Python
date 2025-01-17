seq = ["apple", "banana", "cherry"]
result = ''.join(seq)
#print(result)!!



print('hello world!!')

seq = ["apple", "banana", "cherry", 0.1, True, 123]
result = ', '.join(map(str, seq))
print(result) # 출력 : apple, banana, cherry, 0.1, True, 123