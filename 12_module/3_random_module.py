## python 기본 모듈 - random
import random

## randint(a, b)
print('randint 함수')
for i in range(10):
  print(random.randint(1, 5), end=' ')

'''
randint()
a <= N <= b를 만족하는 정수 N 반환

-> 5 1 2 5 3 1 4 5 2 1 
range()니까 0~9까지 10개의 숫자
randint()라서 1~5 사이의 랜덤한 정수 생성
'''

# -------------------------------------------------------------------------
## randrange(시작, 종료, step)
print('\n\n randrange 함수 1')
for i in range(10):
  print(random.randrange(1, 7), end=' ')

print('\n\n randrange 함수 2')
for i in range(10):
  print(random.randrange(1, 7, 2), end=' ')

'''
randrange()
range(시작, 종료, step) 에서 임의로 선택된 요소 반환

range(10)이니까 0~9까지 10개의 숫자
1. randrange(1, 7)이므로 1~6 사이의 난수 생성
2. randrange(1, 7, 2)라서 1부터 2씩 증가하며 난수 생성
-> 1, 3, 5 만 랜덤으로 10개 출력
'''
# -------------------------------------------------------------------------
## choice(list)
print('\n\n choice 함수')
fruit = ["apple", "banana", "cherry"]
for i in range(5):
  print(random.choice(fruit), end=' ')

'''
choice(list)
리스트에서 랜덤으로 요소 반환

range(5)니까 0~4까지 5개 요소 출력
choice(fruit)여서 리스트에 있는 요소 5개 랜덤 출력
'''