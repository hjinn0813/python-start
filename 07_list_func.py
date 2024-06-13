## sort() - 요소 정렬하기
num = [3, 2, 5, 4, 1]
num.sort()
print(num)
'''
숫자는 크기 순서로 정렬
-> [1, 2, 3, 4, 5]
'''

korean = ['강', '이', '정', '박', '최']
korean.sort()
print(korean) 
# -> ['강', '박', '이', '정', '최']

english = ['b', 'c', 'a', 'd', 'e']
english.sort()
print(english)
# -> ['a', 'b', 'c', 'd', 'e']
# 글자는 알파벳/가나다 순으로 정렬된다.

# -------------------------------------------------------------------------
## reverse() - 순서 뒤집기
'''
현재 순서 그대로 뒤집는 것을 의미한다.
(오름차/내림차순으로 정렬하는게 아님)
'''

num = [3, 2, 5, 4, 1]
print("원래 형태:", num)

num.reverse()
print("reversed:", num)
# -> reversed: [1, 4, 5, 2, 3]

# -------------------------------------------------------------------------
## 요소 추가하기 - append(), insert(), extend()

## append(요소) - 리스트 맨 뒤에 추가
num = [3, 2, 5, 4, 1]
num.append(7)
num.append(9)
print(num)
'''
해당 리스트 맨 뒤에 요소가 추가된다.
-> [3, 2, 5, 4, 1, 7, 9]
'''

## insert(위치, 요소)
korean = ['강', '이', '정', '박', '최']
korean.insert(1, '김')
print(korean)
'''
첫번째 인자에서 지정한 위치에 요소를 집어넣는다.
-> ['강', '김', '이', '정', '박', '최']
'''

## extend(리스트)
english = ['b', 'c', 'a', 'd', 'e']
english.extend(['x', 'y', 'z'])
print(english)
'''
리스트에 또 다른 리스트 추가.
english 리스트의 맨 끝에 extend()에 인자로 들어간 리스트의 요소들이 추가된다.
-> ['b', 'c', 'a', 'd', 'e', 'x', 'y', 'z']
'''

# -------------------------------------------------------------------------
## 요소 삭제하기 - pop(), del, remove(), clear()

## pop(위치)
name = ['강', '정', '이', '박', '정', '최', '오', '윤']
print("원래 상태: ", name)
name.pop(0)
# -> '강'
print("삭제 완료: ", name)
# -> ['정', '이', '박', '정', '최', '오', '윤']

name.pop()
# -> '윤'
print("삭제 완료: ", name)
# -> ['정', '이', '박', '정', '최', '오']

'''
pop(인덱스)
- 인자로 들어가는 인덱스로 요소를 삭제한다.
- 인자가 없으면 리스트의 마지막 요소를 삭제한다.
'''

## del
name = ['강', '정', '이', '박', '정']
del name[2]
print(name)
# -> ['강', '정', '박', '정']

name = ['강', '정', '이', '박', '최', '오', '윤']
del name[3:]
print(name)
# -> ['강', '정', '이']

'''
del 리스트명[인덱스]
- 해당 인덱스 위치의 요소를 삭제한다.
- 범위를 지정해 한번에 요소를 삭제할 수 있다.
'''

## remove(요소)
name = ['강', '정', '이', '박', '정', '최']
name.remove('정')
print(name)
# -> ['강', '이', '박', '정', '최']
'''
remove(요소)
- 리스트에서 요소 이름으로 삭제하는 방법
- 리스트에 같은 요소가 있으면 맨 앞에 것만 삭제
'''

## clear() - 모든 요소 삭제하고 빈 리스트 출력
name.clear()

# -------------------------------------------------------------------------
## index() - 요소 위치 찾기
colors = ['초록', '노랑', '보라', '파랑', '노랑']
idx1 = colors.index('보라')
print(idx1) # -> 2

idx2 = colors.index('노랑')
print(idx2) 
'''
같은 요소가 있으면 맨 앞의 인덱스 번호 출력 
-> return '1'
'''

# -------------------------------------------------------------------------
## count() - 요소 개수 세기
nums = [1, 3, 7, 2, 3, 7, 4, 9, 7, 5]
n = nums.count(7)
print(n) # -> 3

english = ['R', 'o', 'l', 'l', 'e', 'r']
eng = english.count('r')
print(eng)
# 대소문자를 구분하기 때문에, return '1'