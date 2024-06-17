## python 함수 정의하기
# 함수를 만들 때는 'def'라는 키워드 사용 (define의 약자)
def hello1():
  print("study python!")

hello1()

# -------------------------------------------------------------------------
## 함수의 종류
## 1. 입력값 x, 결과값 x
def say_hello3():
  print('hello')
  print('hello')
  print('hello')

say_hello3()

# -------------------------------------------------------------------------
## 2. 입력값 o, 결과값 x
def say_hello(n):
  for i in range(n): 
    print('hello')

say_hello(3)

'''
hello
hello
hello
'''

def hello2(name):
  print("Hello!")
  print(name)

hello2("Linda")

'''
Hello
Linda
'''

# -------------------------------------------------------------------------
## 2-1. 다수의 매개변수 넘기기
def number_sum(a, b):
  print(a + b)

number_sum(3, 5)

def comparison(x, y):
  if x > y:
    print(x, '가 더 크다')
  elif x < y:
    print(y, '가 더 크다')
  else:
    print(x, '=', y, '서로 같다')

comparison(2, 4) # 4가 크다
comparison(3, 1) # 3가 크다
comparison(7, 7) # 7=7 같다

# -------------------------------------------------------------------------
## 3. 입력값 x, 결과값 o
def say_yes():
	return 'Yes!'

print(say_yes()) # -> yes!!!

def func_return():
	return # 결과값 없음

print(func_return()) 
# -> 결과값이 없어서 None 출력

# -------------------------------------------------------------------------
## 4. 입력값 o, 결과값 o
def square_area(width, height):
  return width * height

a = 3
b = 4
print(square_area(a, b)) # 12

# -------------------------------------------------------------------------
## 함수 내부에서 함수 호출하기
def first(n):
  return n * 2

def second():
  x= first(3) + 5 
  # 내부에서 first() 함수 호출 -> 3 * 2 + 5
  return x

print(second()) # 11

# -------------------------------------------------------------------------
# 매개변수와 인자
def what_to_say(param1):
  print(param1)
what_to_say("Hello", "World")
'''
- 매개변수는 함수 정의 시에 값을 받을 변수의 이름
- 인자는 호출 시에 함수에 넘겨주는 값
- 매개변수와 인자의 개수는 동일해야 한다.
위 코드처럼 매개변수는 1개인데 인자가 2개면 오류 발생.
'''

def addition(n):
  sum = 0
  for i in range(n):
    sum = sum + i
  return sum
print(addition(10))
'''
for문 range()에서 0~9까지 반복하면서 누적 덧셈
i + sum = sum
1 + 0 = 1
2 + 1 = 3
3 + 3 = 6
4 + 6 = 10
'''