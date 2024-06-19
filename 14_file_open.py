## 파일 입출력
'''
파일에 저장된 내용을 읽고 쓰는 법.
아주 많은 양의 데이터도 파일에 저장해 보관할 수 있음.
데이터가 추가되면 파일에 해당 내용을 추가한다.
'''

# -------------------------------------------------------------------------
## 파일 열고 닫기
'''
파일 객체 = open(이름, 읽기모드)

파일 객체: 열고자 하는 파일을 담은 변수
파일 읽기 모드: 파일을 읽는 방법 지정
- r (read) 읽기 모드. 기본값. 파일을 읽기만 할때 사용.
- w (write) 쓰기 모드. 새로 파일을 만들어 내용을 작성.
이미 존재하는 파일을 이걸로 열면 기존 내용 지우고 덮어쓰기 된다.
- a (append) 추가 모드. 파일의 맨 마지막에 내용을 추가할 때 사용.

첫번째 매개변수는 정확한 파일의 경로를 의미한다.
'''

# 파일 이름만 작성
# a.txt와 .py 파일이 같은 위치
file1 = open('a.txt', 'r') 

# 전체 경로 작성
# b.txt와 .py 파일이 다른 위치
file2 = open('C:\Users\pc\Desktop\b.txt', 'r') 

'''
파일_객체.close()
- 프로그램이 종료될 때 열려 있는 파일이 알아서 종료되기 때문에 
명시적으로 close()를 작성하는 습관을 들이면 예상치 못한 오류를 방지할 수 있다.
- 쓰기 모드로 열었던 파일을 종료하지 않고 다시 열면 오류가 발생함!
'''

# -------------------------------------------------------------------------
## 파일 쓰기 - w(write)
file = open('first.txt', 'w')
file.write('Very Nice!! \n이건 내가 만든 첫 번째 파일>_< \n') 
file.close()
'''
- w 모드로 first.txt 파일 열기
- write()로 파일에 내용 작성하기
- close()로 파일 닫기
'''

# -------------------------------------------------------------------------
'''
with 키워드
- 파일을 열고 with 블록을 벗어날 때 자동으로 닫아주어
매번 close() 함수로 파일을 닫는 번거로움을 줄일 수 있다.
'''

with open('first.txt', 'w') as file:
  file.write('Very Nice!! \n이건 내가 만든 첫 번째 파일>_< \n')
  
# -------------------------------------------------------------------------
## 파일에 내용 추가하기 - a(append)
with open('first.txt', 'a') as file:  
  file.write('여기는 내용 추가한 부분~!')
  
# -------------------------------------------------------------------------
## 파일 읽기 - r(read)
with open('lyrics.txt', 'r', encoding='UTF8') as file:
  blueming = file.read()
print(blueming)

'''
파일객체.read()
-> txt 파일에 저장된 전체 텍스트 출력

- python 버전3은 파일을 읽을 때 ANSI 기준으로 작성된 것만 가능.
파일 오픈 시에 인코딩 형식을 UTF-8로 지정해 에러 발생 방지.
'''

## readline()
with open('lyrics.txt', 'r', encoding='UTF8') as file:
  while True:
    blueming = file.readline()
    if blueming == None: # 더 이상 읽을 내용이 없음
      break
    print(blueming, end='')

'''
파일객체.readline()
- 한 번에 한 라인만 읽는 함수
- 파일 끝에 도착하여 더이상 읽을 라인이 없으면 None 반환
(그러므로 while을 사용하여 내용을 한 줄씩 출력할 수 있음)
'''

## readlines()
with open('lyrics.txt', 'r', encoding='UTF8') as file:
  blueming = file.readlines()
print(blueming)

'''
파일객체.readlines()
- 모든 라인을 리스트에 하나씩 저장하는 함수
- 각 요소에 줄바꿈 문자(\n)도 함께 저장한다
'''

with open('b.txt', 'w') as file:
  file.write('one\n two\n three\n four\n five\n')

with open('b.txt', 'r', encoding='UTF8') as file:
  song = file.readlines()
  print(song)
  print(len(song))

'''
readlines()는 각 라인을 리스트에 하나씩 저장
-> print(song)은 file.write()로 작성한걸 리스트에 저장
-> ['one\n', 'two\n', 'three\n', 'four\n', 'five\n'] 출력
-> print(len(song))은 리스트의 길이를 요구하므로 '5' 출력
'''