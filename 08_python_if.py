## python의 조건문

if 5 < 7 :
  print('Smaller!')
  # if의 조건이 true니까 'Smaller!' 출력

if 5 > 7:
  print('Bigger!')
  # if의 조건이 false라서 출력되지 않음

# 값을 입력받아 조건에 따라 다른 문장 출력하기
n = int(input('숫자를 입력하세요'))
if n % 2 == 0: 
  print('짝수입니다!')
if n % 2 != 0:
  print('홀수입니다!')
  
## if ~ else ~
if n % 2 == 0: 
  print('짝수입니다!')
else:
  print('홀수입니다!')

## if ~ elif ~ else
x = 10
if x < 4:
  print('small')
elif x < 8:
  print('medium')
elif x < 12:
  print('large')
else:
  print('extra large')

## 조건문 순서의 중요성
y = 5
if y < 2:
	print('Small')
elif y < 4 :
	print('Medium')

'''
y라는 변수에 5를 할당했지만
if와 elif에 해당하는 조건에 모두 만족하지 않으므로
위 코드는 아무 것도 출력하지 않는다.

-> else 생략 가능하나,
조건을 만족하지 않으면 아무 것도 출력되지 않을 수 있다.
'''

a = int(input("숫자 입력: "))
if a < 10:
  print('Black')
elif a < 20:
  print('Red')
elif a < 40:
  print('Yellow')
elif a < 30:
  print('Blue')
else:
  print('Done')

'''
if문은 위에서 아래로 내려가면서 조건에 맞는지 비교하는데
위 코드에서는 조건 지정하는 순서가 잘못되었기 때문에, 
a에 어떤 숫자가 와도 'a < 30' 조건에 해당하는 값은 출력될 수 없다.
'''