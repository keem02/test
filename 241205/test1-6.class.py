# class Car(object): #앞 부분을 대문자로 사용합니다. ref.(object)없어도 된다
# 	MaxSpeed = 300
# 	MaxPeople = 5
# 	def move(self, x):
# 		print(x, '의 스피드로 움직이고 있습니다.')
# 	def stop(self):
# 		print('멈췄습니다.')

# k5 = Car()
# k3 = Car()
# k5.move(10)
# k5.stop()
# k3.move(5)
# k3.stop()

# print(k5.MaxSpeed)
# print(k3.MaxSpeed)




# 1. car 클래스에서 함수를 만든다. 함수 이름은 change_brand, 함수는 brand 값을 변경해야한다.
# 2. 멤버 변수에는 brand가 있어야한다. 그 변수는 기본적으로 값이 없다.
# 3. 외부에서 change_brand 호출해서 값을 바꾼다.

# class Car(object)
# 	def brand()
	
	




# 1. Human 이라는 클래스를 만들고
# 2. 인스턴스 변수는 각각 name(이름), gender(성별), 나이(age) 를 가지고 있어야한다.
# 3. __init__ 메서드를 통해 각 위 인스턴스 변수를 초기화한다.
# 4. 각 인스턴스 변수를 출력할 함수를 만든다. ( 출력형태는 자유)
# 5. 인스턴스를 만들어 함수를 호출해본다.

class human:
	def __init__(self, name, gender, age) -> None:
        self.name = name
		self.gender = gender
		self.age = age
		
    
print(self.name)
# class Human:
#     # __init__ 메서드를 통해 인스턴스 변수 초기화
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     # 인스턴스 변수를 출력하는 함수
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Gender: {self.gender}")
#         print(f"Age: {self.age}")

# # Human 클래스 사용 예시
# person = Human(name="Alice", gender="Female", age=30)  # 인스턴스 생성
# person.display_info()  # 인스턴스 변수 출력

Man = Human("뀨","남자",11)
woman = Human("뀨2","여자",5)
	






class Human:

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age

    def print_name(self):
        print(self.name)

    def print_gender(self):
        print(self.gender)

    def print_age(self):
        print(self.age)


man = Human("뀨","남자",11)
woman = Human("뀨2","여",10)

man.print_name()
woman.print_name()

man.print_gender()
woman.print_gender()

man.print_age()
woman.print_age()