def decorator1(func):
    def wrapper(x):
        result = func(x)
        print(f'Decorator 1 result : {result}')
        return result
    return wrapper

def decorator2(func):
    def wrapper(x):
        result = func(x)
        print(f'Decorator 2 result : {result}')
        # 추가로 decorator1의 wrapper 함수를 호출하고, 결과값을 사용
        return decorator1(func)(x)
    return wrapper

@decorator2
def add(x):
    x += 1
    return x

print(add(1))
