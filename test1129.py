"""
a = 10
b = 3

# print(f'10 + 3', {a + b})
print(f'10 + 3 == {a + b}')
"""

"""
# 2교시

numA = 25
numB = 40

print

numA = 1
NumA = numA + 1
# numA /= 
"""
"""
a = 10
b = 3

print(f'10 + 3 == {a + b}')
print(f'10 - 3 == {a - b}')
print(f'10 / 3 == {a / b}')
print(f'10 // 3 == {a // b}')
print(f'10 * 3 == {a * b}')
print(f'10 ** 3 == {a ** b}')
print(f'10 % 3 == {a % b}')
"""
"""
a = True  # 1
b = False # 0

#and : 논리곱
#or  : 논리합
#not : 부정

a and b #여기서부터는 한 줄씩 실행해보세요.
a and a
b and b
b and a
b and (b and c and d and e)
b and (b and ccc and ddd and eee)

"""
"""
print(a or b)
print(a or a)
print(b or b)
print(b or a)
print(b or (b and ccc and ddd and eee))
print(b or (b or ccc or ddd or eee))


print(a or b)
print(a or a)
print(b or b)
print(b or a)
print(b or (b and ccc and ddd and eee)) # c d e 선언되어 있지 않아도 b값이 있으므로 and 이기 떄문
"""
a = True  # 1
b = False # 0

#and : 논리곱
#or  : 논리합
#not : 부정

# print(b or (b or ccc or ddd or eee)) # c가 없으니까 안나옴 or 이기 때문에


print(not a)
a + a
b + a
b + b
b - a

bool(b-a)


# 3교시

for i in range(100):
    if i % 3 == 0 and i % 5 ==0:
        print(i)