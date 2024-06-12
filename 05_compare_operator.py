### 비교연산자 (결과는 불리언으로 출력)

## 같음, 같지 않음
print(1 == 2) # false
print(1 != 2) # true

## 크다, 작다
print(1 < 2) # true
print(1 > 2) # false

## 크거나 같음, 작거나 같음
print(1 <= 2) # true
print(1 >= 2) # false

# -------------------------------------------------------------------------
## 문자열 비교 연산
print("star" == "apple") # false
print("star" != "apple") # true
print("star" > "apple") # true
print("star" < "apple") # false

'''
문자열의 비교연산은 알파벳/가나다 순서대로 진행
먼저 등장하는 알파벳이 작다. (ex. a < b)
'''

# -------------------------------------------------------------------------
## 논리연산자

# not 연산자 (결과 뒤집기)
print(not True)
print(not False)

# and 연산자 (둘 다 참이어야 참)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or 연산자 (하나만 참이어도 참)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# -------------------------------------------------------------------------
## QUIZ
print("lemon" > "lucky") 
'''
(e > u) -> false
-> return 'false'
'''

print((1 > 2) == False) 
'''
(1 > 2) -> false
print(false == false)
-> return 'true'
'''

print(not 5 < 5) 
'''
(5 < 5) -> false
print(not false)
-> return 'true'
'''

print(False and (10 != 2)) 
'''
(10 != 2) -> true
print(false and true)
-> return 'false'
'''

