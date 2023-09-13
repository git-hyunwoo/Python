x = 29
y = x + 1

print(f'id(x) : {id(x)}')
print(f'id(y) : {id(y)}')

if id(x) == id(y):
    print("둘의 메모리 주소는 같습니다")
else:
    print("둘의 메모리 주소는 같지 않습니다")