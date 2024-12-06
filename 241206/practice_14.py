숫자 = [1, 2, 3, 4, 5]
승수 = [2, 2, 2, 3, 3]
# 1.
li = list(zip(숫자, 승수))


def test(x):
    return x >= 100

def test1(x: tuple):
    return x[0] ** x[1]


a = list(map(test1, li))
print(a)
b = list(filter(test,a))
print(b)