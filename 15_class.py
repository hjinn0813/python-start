## python class

'''
~~ 기본구조 ~~
class 클래스명:
  필드
  메소드

- 클래스명은 CamelCase로 작성
'''

class Person:
  def say_hello(self):
    print('Hi!! Nice to meet you.')

p = Person() # 객체 p에 클래스 할당
p.say_hello() # 클래스에 들어있는 메소드 호출

# -------------------------------------------------------------------------
## init 메소드
class Person:
  count = 0 # 클래스 변수
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.count = Person.count + 1 # 객체가 생성될 때마다 증가 

  def say_hello(self):
    print('Hi!! Nice to meet you.')

  def about_me(self):
    print('I am ' + self.name + ' (' + str(self.age) + ')')

suzy = Person('Suzy', 20)
suzy.say_hello()
suzy.about_me()

'''
Person이라는 클래스를 만들고 내부에 메소드 생성.
suzy라는 객체를 만들어서 클래스에 이름, 나이 할당.
해당 객체에 들어있는 이름(suzy)과 나이(20)가 초기값이 된다.

Person 클래스가 만들어졌기 때문에,
아래와 같이 다른 객체도 생성 가능하다.
'''

minho = Person('Minho', 23)
minho.say_hello()
minho.about_me()
print('** 총 ' + str(Person.count) + '명 **')

yeji = Person('Yeji', 21)
yeji.say_hello()
yeji.about_me()
print('** 총 ' + str(Person.count) + '명 **')

# -------------------------------------------------------------------------
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def birth_year(self):
    now_year = 2022
    birth_year = str(now_year - self.age + 1)
    print(birth_year)

  def say_name(self):
    print(self.name)

  def change_name(self, new_name):
    self.name = new_name

dog1 = Dog('Coco', 5)
dog1.change_name('Luna')
dog1.say_name()

'''
change_name은 new_name이라는 인자를 받고 있으므로
호출할때 인자를 넣어야 에러가 발생하지 않는다.
'''