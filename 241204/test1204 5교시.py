# 1. 1부터 1000까지의 리스트 생성
numbers = list(range(1, 1001))

# 2. 리스트 컴프리헨션을 사용해 2의 배수 또는 5의 배수인 숫자만 필터링
filtered_numbers = [num for num in numbers if num % 2 == 0 or num % 5 == 0]

# 3. 필터링된 리스트의 전체 합 계산
total_sum = sum(filtered_numbers)
print("리스트의 전체 합:", total_sum)

# 4. 필터링된 리스트의 길이 계산
length = len(filtered_numbers)
print("리스트의 길이:", length)




# 1. 1부터 1000까지의 리스트 생성
numbers = list(range(1, 1001))

# 2. 리스트 컴프리헨션으로 2의 배수 또는 5의 배수인 리스트 생성
def is_multiple_of_two_or_five(num):
    return num % 2 == 0 or num % 5 == 0

special_numbers = [num for num in numbers if is_multiple_of_two_or_five(num)]

# 3. special_numbers 리스트의 전체 합 구하기 및 출력
total_sum = sum(special_numbers)
print(f"2의 배수 또는 5의 배수의 합: {total_sum}")

# 4. special_numbers 리스트의 길이 구하기 및 출력
list_length = len(special_numbers)
print(f"2의 배수 또는 5의 배수의 개수: {list_length}")




# li = list(range(1,1001))

# def filtering(x)
#     if x % 2 == 0 or x % 5 == 0
#         return x
#     else:
#         return None




# b = [ x for x in a if x % 2 == 0 or x % 5 == 0 ]
# 이렇게 하긴 했는데
# 이게 함수를 써서는.. 뭔가 생각이 안들더라고요 None을 없앨 방법이



# new li = 


# a = 1
# while a < 10 :
# 	print(a)
# 	a += 1 



    #pass
구매개수_총가격= [
    (3, 15000),
    (5, 25000),
    (1, 5000),
    (8, 40000),
    (0, 0),
    (2, 10000)
    ]
for 구매개수, 총가격 in 구매개수_총가격:
    if 구매개수 < 1:
        pass
    print('구매개수는 {}개이며 {}원입니다.'.format(구매개수, 총가격))




    #for, else문
for i in range(5, 0, -1):
    print("고등어 ", i, " 개 남았습니다.")
else:
    print('고등어 다 팔렸습니다.')



# 입력받은 숫자가 소수인지 판별하세요
# 소수: 1과 자기 자신으로만 나누어지는 수
# 예: 입력 = 7, 출력 = "소수입니다"

num = int(input("enter a number: "))
is_prime = True
if num <= 2





# 주어진 리스트에서 중복된 숫자를 제거하고 오름차순으로 정렬하세요
# 예: 

# 입력 = [1, 3, 3, 5, 1, 2, 7, 5]
# 출력 = [1, 2, 3, 5, 7]


numbers = [1,3,3,5,1,2,7,5]
result = []
# 중복제거
for num in numbers:
    exits = False
    for unique in result:
        if num == unique:
            exits = True
            break
    if not exits:
        result.append(num)

data = sorted(result)

print(data)