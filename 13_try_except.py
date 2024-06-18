## python 예외처리

'''
~~ 기본구조 ~~
try:
	예외가 발생할 수 있는 문장
except 오류 종류:
	예외를 처리하는 문장
'''

# -------------------------------------------------------------------------
try:
	num = int(input('정수 입력: '))
except ValueError:
	print('정수가 아님! 정수를 입력해주세요!')

'''
- 예외가 발생할 수 있는 문장을 try에 작성
- 오류 종류를 except절에 작성
- 예외처리 안내 메시지를 except 아래에 작성
'''

while True: # 무한 반복
	try:
		num = int(input('정수 입력: '))
		break # 정수 입력시 반복문 탈출
	except ValueError: # 예외 처리
		print('정수가 아님!')

# -------------------------------------------------------------------------
## as 키워드

'''
~~ 기본구조 ~~
try:
	예외 발생할 수 있는 문장
except 발생 오류 as 오류 메세지 변수:
	예외 발생시 실행할 문장
'''

try:
  color = ['purple', 'yellow', 'green', 'blue']
  for x in color:
    print(color.index(x))
  print(color.index('orange'))
except ValueError as message:
  print(message)

'''
as 키워드: 시스템에서 출력하는 오류 메시지로 예외처리

예시의 리스트에는 'orange'가 없기 때문에 ValueError가 발생
-> as 키워드로 기본적인 오류 메시지를 출력하도록 설정
-> 'orange' is not in list 출력
'''

# -------------------------------------------------------------------------
## except에서 에러 종류 생략 가능
try:
  x = int(input('정수 입력> '))
  y = int(input('정수 입력> '))
  print(x/y)
except:
  print('0으로 나눌 수 없음!!')

'''
except 절에는 오류의 종류를 명시해야 하지만 생략 가능.
단, 생략하면 모든 오류에 대해 하나의 except 실행.
'''

# -------------------------------------------------------------------------
## 다중 예외 처리: try ~ except ~ else

'''
~~ 기본구조 ~~
try:
	예외가 발생할 수 있는 문장
except 오류종류1:
	예외를 처리하는 문장
except 오류종류2:
	예외를 처리하는 문장
else:
	예외가 없는 경우에 실행 (else절은 생략 가능)
'''

# try에서 상황을 확인하고 첫번째 except 출력
try:
  num = [1, 2, 3, 4]
  print('START')
  print(num[3]/0) 
  print(num[100])
  print('END')
except NameError:
  print("존재하지 않는 변수 호출")
except IndexError:
  print("인덱스 에러 발생")
except ZeroDivisionError:
  print("0으로 나눌 수 없음!")

# 예외가 없어서 else절 출력
try:
  num = [1, 2, 3, 4]
  for i in num: 
    print(i)
except NameError:
  print("존재하지 않는 변수 호출")
except IndexError:
  print("인덱스 에러 발생")
except ZeroDivisionError:
  print("0으로 나눌 수 없음!")
else:
  print("예외 없음! 성공적!!")
