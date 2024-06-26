## python 기본 문법
# 짧은 주석은 해시태그로 표시한다
'''
긴 주석은 이렇게 따옴표 사이에 표시한다
(큰 따옴표, 작은 따옴표 모두 가능)
'''

# 변수의 자료형에 대한 선언 없음 (저장되는 값에 따라 자동으로 자료형 지정됨)
# 문장의 끝에 세미콜론(;) 사용할 필요 없음 (한 줄에 여러 문장일 때만 사용)
num = 1; print(num)

# 코드블록이 있으면 콜론(:)과 여백으로 구분한다
# 변수에 연속해서 값 저장 가능
x,y,z = 10,20,30
print(x + y - z)

# ------------------------------------------------------------------------------
## python 기본 출력함수, print()
print(20)
print(3 + 3)
print() # 괄호에 아무것도 입력하지 않으면 빈값 출력

## python 기본 입력함수, input()
hobby = input('너의 취미는?')

'''
- input()으로 받는 데이터는 무조건 문자열로 저장된다.

- IDLE 입력기에서 'input(출력문자)' 입력하고 enter 치면
해당 출력문자가 화면에 출력되고 사용자의 입력을 기다린다.
답변을 입력하면 해당 답변이 hobby라는 변수에 저장되어,
print(hobby)를 했을 때 변수에 저장된 답변이 출력된다.
'''
