number = 2 + 3 * 4

print(number)

number = number + 2 
print(number)

number += 2
print(number)

number *= 2
print(number)

number /= 2
print(number)

number -= 2
print(number)

number %= 5
print(number)

# 숫자 처리 함수
print(abs(-5)) # 절대값
print(pow(4,2)) # 4^2
print(max(5,12)) # 최대값
print(min(5,12)) # 최소값
print(round(4.99))
print(round(3.14))

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

# 랜덤 함수 = 난수
from random import *

print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random()* 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 생성

print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값

print(randrange(1,45)) # 1 ~ 45 미만의 임의의 값 생성 (45 미포함)

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성 (45 포함)