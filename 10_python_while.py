## python의 반복문 - while
'''
~ 기본구조 ~
while 조건식:
  수행할 문장
반복문이 종료되면 실행할 문장

- 조건식이 true면 반복문 처음부터 다시 실행
- 조건식이 false면 반복문 종료
'''

# while 사용해보기
num = 5
while num >= 0:
  print(num)
  num = num -1

'''
return 5 4 3 2 1 0

num이 0보다 크거나 같을 때 while문 내부의 코드 실행
-> num - 1한 값을 왼쪽의 num에 할당
-> 숫자가 5부터 감소되며 출력
-> 0까지 출력되면 조건을 충족하지 않아서 반복문 종료
'''

# while 무한루프
'''
num = 5
while num >= 0:
	print(num) 
num = num - 1 

-> 마지막 줄에 들여쓰기가 없어서
while문의 조건이 계속 만족되기 때문에 무한루프로 5 출력
무한루프 빠져나오려면 ctrl + c
'''

# break, continue
while True:
	lunch = input("오늘 점심 후보? ")
	if lunch == "그만":
		break
	if len(lunch) <= 3:
		print("그건 안돼")
		continue
	print(lunch)
print("done")

'''
while의 조건식이 true여서 무한루프를 돌게 되는 프로그램이지만
if문과 break를 사용하여 반복문 탈출 조건을 설정할 수 있다.
만약 입력받은 값이 3글자 이하라면 특정 메시지를 출력하고
사용자에게 다시 입력받기 위해 continue를 사용한다.
'''