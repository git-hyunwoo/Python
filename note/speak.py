import random

# 동일한 시드를 사용하여 난수 생성기 초기화
random.seed(29)

# 두 번째 난수 생성
random_num_1 = random.random()
random_num_2 = random.random()

print(random_num_1)  # 출력: 0.5481190538116991
print(random_num_2)  # 출력: 0.34583182333805484 

# 동일한 시드를 다시 사용하여 난수 생성기 초기화
random.seed(29)

# 두 번째 난수 생성 (이전과 동일한 결과를 얻을 것입니다)
random_num_3 = random.random()
random_num_4 = random.random()

print(random_num_3)  # 출력: 0.5481190538116991
print(random_num_4)  # 출력: 0.34583182333805484
