PI = 3.14
# 변수이름 대문자는 상수 

def circle(r,inputpi):
    z = r*r*inputpi
    return z

result = circle(10, PI)
print(result)



def f(a, b, c):
# def f(a, b, c=100): 으로 default 값으로 했을 때 f(100,10) 는 ok    
    print(a, b, c)

# f() # error
# f(100, 10) # error
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)


def f(a, b, c):
    return a * b * c

# f() # error
print(f(100, 10 , 200)) # error
print(f(a=100, b=200, c=300))
print(f(c=300, a=100, b=200))



def f(a=10, b=20, c=30):
    print(a, b, c)

f()
f(100, 10)
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)

f('example')


#sys.setrecursionlimit -> 제한을 늘릴 수 있음
# def 숫자출력():
#     print(1)
#     return 숫자출력()
# 숫자출력()


s = "   hello okay world!   "
s = s.strip()
s = s.replace("okay ", "")
print(s)


# 241202 1시
# 3.2 재귀함수

# def factorial(n):
#     if n == 1:
#         return 1
#     else: 
#     return n * factorial(n-1)
# factorial(5) #factorial(5) = 5 * factorial(4)

# print(factorial(5)) # factorial(5)=5 * factorial(4) * factorial(3) * fac 2 * fac 1 = 5 * 4 * 3 * 2 * 1 



a = 'pithon'

def 함수1():
    def 함수2():
        print('love')
        
    print('I')
    함수2()
    return "python"
	

a = 함수1()
print(a)



# 함수를 이용하여 계산기 프로그램을 만들어주세요. 6 mins

def plus(num1, num2):
	#이곳을 채워주세요

def minus(num1, num2):
	#이곳을 채워주세요

def multiply(num1, num2):
	#이곳을 채워주세요

def divide(num1, num2):
	#이곳을 채워주세요

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')




