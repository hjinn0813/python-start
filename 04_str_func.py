### 문자열에서 사용하는 함수

## len() - 문자열의 길이 추출, length
a = 'Strawberry Moon'
len(a)
'''
-> return 15
공백과 특수문자도 하나의 문자로 인식한다.
'''

## count() - 특정 문자의 개수 구하기
a = 'Strawberry Moon'
a.count('r')
'''
-> return 3
대소문자를 구분하기 때문에 함수에 인자로 들어간 것만 찾아낸다.
'''

## upper(), lower() - 대소문자를 바꿔주는 함수
b = 'hello'
b.upper()
c = 'WORLD'
c.lower()

## strip() - 양쪽 공백 삭제
d = '  welcome  '
d.strip()

## find() - 왼쪽부터 위치 찾기
e = 'Roller Coaster'
e.find('r')
'''
-> return 5
왼쪽부터 찾아서 가장 먼저 발견한 것의 인덱스 번호 출력.
문자열에 없는 알파벳을 찾는다면 -1을 출력한다.
'''

## rfind() - 오른쪽부터 위치 찾기
e = 'Roller Coaster'
e.rfind() 
# -> return 13

## split() - 특정 지점 기준으로 문자열 나누기
e = 'Roller Coaster'
e.split(' ')
# 공백 기준으로 나뉘어서 리스트 ['Roller', 'Coaster'] 출력

x = 'Hello, world'
x.split(',')
# 쉼표 기준으로 나뉘어서 리스트 ['Hello', ' world'] 출력