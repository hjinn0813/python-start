## python의 반복문 - for
'''
~ 기본구조 ~
for 변수 in 리스트:
  실행할 문장1
  
반복문 종료시 실행할 문장
'''

num = [0, 1, 2, 3, 4]
for i in num:
  print(i)

snack = ['홈런볼', '새우깡', '포카칩', '다이제']
for s in snack:
	print(s)

'''
첫번째 반복에서 0번째 인덱스,
두번째 반복에서는 1번째 인덱스..
-> 반복되는 동안 변수에 리스트의 요소가 들어간다.
'''

# -------------------------------------------------------------------------
## range()

a = range(10)
for i in a: 
  print(i, end=' ')
# -> 0 1 2 3 4 5 6 7 8 9

b = range(1, 11)
for i in b:
  print(i, end=' ')
# -> 1 2 3 4 5 6 7 8 9 10

c = range(3, 12, 2)
for i in c:
  print(i, end=' ')
# -> 3 5 7 9 11

d = range(10, 0, -1)
for i in d:
  print(i)
# -> 10 9 8 7 6 5 4 3 2 1

'''
range(n): 0부터 n-1까지의 숫자 출력
range(a, n): a부터 n-1까지의 숫자 출력
range(a, n, b): a부터 b씩 증가한 숫자를 n-1까지 출력
'''

# end는 연속적으로 출력할 수 있게 도와주는 키워드
print('010', end='-')
print('1234', end='-')
print('5678')

'''
이렇게 입력하면 문자열 끝에 '-'가 붙어서
'010-1234-5678' 출력된다.
'''

# -------------------------------------------------------------------------
## for문과 range() 함께 사용하기

numbers = [1, 22, 333, 4444, 55555]

for n in range(len(numbers)): 
  print(str(n) + "번째 값: " + str(numbers[n]))

'''
0번째 값: 1
1번째 값: 22
2번째 값: 333
3번째 값: 4444
4번째 값: 55555

-> range()에 인자로 len(numbers)을 넣어서, 리스트 길이만큼 반복문 실행
print에서 문자열 덧셈을 위해 숫자들을 형변환시킴.
리스트 요소 출력 시에는 인덱스로 접근하여 출력.
'''

# -------------------------------------------------------------------------
## for문과 리스트 함께 사용하기

nums = []

for i in range(1, 11):
	nums.append(i)

print(nums)

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

-> for문에서 range로 1부터 10까지 숫자 입력할거라고 지정.
반복문으로 받은 숫자들을 nums라는 빈 배열에 append()로 삽입.
'''

# -------------------------------------------------------------------------
## for문과 if문 함께 사용하기
score = [54, 97, 99, 36, 82]

for x in score:
  if x >= 80:
    print(x, ":합격")
  else:
    print(x, ":불합격")

# -------------------------------------------------------------------------
## 이중 for문
for y in range(5): # 외부 반복문
  for x in range(1, 11): # 내부 반복문
      print(x, end=" ")
  print() # 내부 반복문이 종료될 때마다 실행

'''
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 

-> 내부 반복문에서 1 ~ 10까지의 숫자를 출력할거라고 설정.
외부 반복문에서 1 ~ 10까지 출력하는걸 5번 반복하라고 설정.
즉, y가 0일 때부터 4까지 내부 반복문을 실행한다.
'''

## 이중 for문으로 별 그리기
for i in range(1, 5):
  for j in range(1, 11):
    print("*", end="")
  print()

'''
**********
**********
**********
**********

-> 내부 반복문에서 (1 ~ 10까지) 10개의 별을 입력하라고 설정.
외부 반복문에서 해당 출력을 4번 반복하라고 설정.
즉, i가 1일 때부터 4까지 내부 반복문을 실행한다.
'''

for i in range(1, 6):
  for j in range(1, i+1): 
    print("*", end="")
  print()
  
'''
*
**
***
****
*****

-> 내부 반복문에서 1부터 i+1까지 별을 출력하라고 설정하여
반복이 거듭될수록 별의 개수가 늘어난다. (1 <= j < i+1)
외부 반복문에서 해당 출력을 1부터 5까지 5번 반복하라고 설정.
'''