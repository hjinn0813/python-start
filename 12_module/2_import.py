## python 모듈

## 모듈 불러오기 1. 모듈명.함수명
import python_module

print("**** 숫자 입력 ****")
x = int(input('x 는 > '))
y = int(input('y 는 > '))

print("\n**** 결과 출력 ****")
print(x, "+", y, "=", python_module.add(x, y))
print(x, "-", y, "=", python_module.sub(x, y))
print(x, "*", y, "=", python_module.multiply(x, y))
print(x, "/", y, "=", python_module.divide(x, y))

# -------------------------------------------------------------------------
## 모듈 불러오기 2. from ~ import ~
from python_module import add, multiply

print("**** 두 수 입력 ****")
x = int(input('x 는 > '))
y = int(input('y 는 > '))

print("\n**** 결과 출력 ****")
print(x, "+", y, "=", add(x, y))
print(x, "*", y, "=", multiply(x, y))
# 이때 from import에서 지정하지 않은 함수를 사용하면 NameError 발생

# -------------------------------------------------------------------------
## 모든 것을 의미하는 별표
from python_module import *

print("**** 숫자 입력 ****")
x = int(input('x 는 > '))
y = int(input('y 는 > '))

print("\n**** 결과 출력 ****")
print(x, "+", y, "=", add(x, y))
print(x, "-", y, "=", sub(x, y))
print(x, "*", y, "=", multiply(x, y))
print(x, "/", y, "=", divide(x, y))