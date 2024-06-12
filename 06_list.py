## 리스트 자료형
'''
시퀀스(Sequense) 자료형에 속하는 데이터 타입

~~ 리스트 자료형의 특징 ~~
1. 새로운 항목 추가, 삭제 가능
2. 항목에 대한 순서가 있다
3. 항목 검색 가능

-> 순서대로 정리된 항목을 담고있는 데이터
(JS의 배열 데이터 같음)
'''

# 리스트 자료형의 기본 구조
fruit = ['berry', 'orange', 'peach', 'kiwi']

# 리스트 안에 리스트 담기
fruits = [['blueberry','strawberry'], 'orange', 'peach', 'melon', 'kiwi']

# 다양한 자료형 모두 담기 가능
basket = [4, 30, ['hello', '안녕'], '파이썬']

# 빈 리스트
empty = []

# -------------------------------------------------------------------------
## 리스트의 인덱싱, 슬라이싱
fruits = [['blueberry','strawberry'], 'orange', 'peach', 'melon', 'kiwi']

## 리스트 인덱싱
print(fruits[0]) # ['blueberry', 'strawberry']
print(fruits[3]) # melon
print(fruits[-1]) # kiwi
print(fruits[0][1]) # strawberry

## 리스트 슬라이싱
print(fruits[0:3]) # [['blueberry','strawberry'], 'orange', 'peach']
print(fruits[:2]) 
'''
시작위치가 생략되면 0번 인덱스부터
-> [['blueberry','strawberry'], 'orange']
'''

print(fruits[-3:]) 
'''
종료위치가 생략되면 마지막 데이터까지
-> ['peach', 'melon', 'kiwi']
'''

print(fruits[0][0:1]) # ['blueberry']
print(fruits[0][1:]) # ['strawberry']

# -------------------------------------------------------------------------
## 리스트 연산하기
color1 = ['yellow', 'purple']
color2 = ['green', 'blue', 'navy']

print(color1 + color2)
'''
두 리스트가 더해져서 새로운 리스트가 출력된다.
-> ['yellow', 'purple', 'green', 'blue', 'navy']
'''

print(color1 * 3)
'''
요소들을 지정된 횟수만큼 반복 출력한 새로운 리스트 생성
-> ['yellow', 'purple', 'yellow', 'purple', 'yellow', 'purple']
'''

# 리스트 길이 구하기
print(len(color1))
print(len(color2))

# -------------------------------------------------------------------------
# 리스트 요소 수정하기
cart = ['blue shirt', 'white hat', 'potato']
cart[1] = 'red hat'
print(cart) # ['blue shirt', 'red hat', 'potato']