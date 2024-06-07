## python 데이터 타입
# 정수 (integer)
print(2)
print(2 + 7)

# 소수 (floating point)
print(2.0)

# 문자열 (string)
print("hello world")
print("2")
print("2" + "7")

# 불리언 (boolean)
print(3 < 7)
print(2 > 5)

# ------------------------------------------------------------------------------
## 데이터타입을 확인하는 함수, type()
type(77)
type(12.5)
type('77')

# ------------------------------------------------------------------------------
## 이스케이프(escape) 문자
# print()에서 따옴표를 이중으로 사용할 때, 문장이 아직 안 끝났다고 표시하는 방법
print('what\'s your name?')
print("\"안녕\"이라고 인사했다")

# 백슬래시를 출력하고 싶은 경우
print('오렌지\\사과')

# 줄바꿈하려면 \n
print('첫번째 줄\n두번째 줄')

# 문장 사이에 탭을 적용하려면 \t
print('첫번째 문장\t탭 적용한 두번째 문장')

# ------------------------------------------------------------------------------
## 형변환 함수
'''
- input()이 받아오는 데이터는 반드시 문자열로 저장된다.
이걸 다른 데이터타입으로 변환하려면 형변환 함수를 사용해야한다.

- 숫자형끼리의 형변환은 자유롭다.
'''

## int() - 문자형을 정수형으로 
favorite_num = input("가장 좋아하는 숫자는?")
print(favorite_num)
print(type(favorite_num)) # 데이터타입 확인 -> <class 'str'>

favorite_num = int(favorite_num) # 형변환
print(type(favorite_num)) # 데이터타입 확인 -> <class 'int'>

## float() - 문자형을 실수형으로
pi = input("원주율은 얼마?")
print(pi) # 3.14
print(type(pi)) # 데이터타입 확인 -> <class 'str'>

pi = float(pi)
print(type(pi)) # 데이터타입 확인 -> <class 'float'>

## 문자열인 소수를 정수형으로 (문자 ~ 실수 ~ 정수 순서)
my_num = float("1.23") # 문자를 실수형으로 변환
print(my_num)
print(int(my_num)) # 실수를 정수형으로 변환

## srt() - 숫자형을 문자형으로
age = 20
print(type(age)) # 데이터타입 확인 -> <class 'int'>

age = str(age) 
print(type(age)) # 데이터타입 확인 -> <class 'str'>