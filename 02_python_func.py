## python 함수 정의하기
# 함수를 만들 때는 'def'라는 키워드 사용 (define의 약자)
def hello1():
  print("study python!")

hello1()

# ---------------------------------------------------------------------
## python의 파라미터 넘기기
def hello2(name):
  print("Hello!")
  print(name)

hello2("Linda")

## 다수의 파라미터 넘기기
def number_sum(a, b):
  print(a + b)

number_sum(3, 5)