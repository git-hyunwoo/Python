seq = ["apple", "banana", "cherry"]
result = ''.join(seq)
#print(result)





my_list = ["apple", "banana", "cherry", 0.1, True, 123]
result = ', '.join(map(str, my_list))
print(result)