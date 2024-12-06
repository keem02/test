print(hex(100))
print(oct(100))
print(bin(100))


"""
문제: 정수들이 담긴 리스트가 주어질 때, 각 정수를 3배로 만들어 반환하는 함수를 작성하세요.
map() 함수를 사용해야 합니다.

입력 예시: [1, 2, 3, 4, 5]
출력 예시: [3, 6, 9, 12, 15]

요구사항:
1. map() 함수를 사용하세요
2. multiply_by_three 함수를 정의하여 사용하세요
"""


ultiply_by_three = [1, 2, 3, 4, 5]

def multiply_by_three(x):
    return x * 3
print(list(map(multiply_by_three, list(list1))))


# def multiply_by_three(numbers):
#     # 각 숫자를 3배로 만드는 함수와 map() 사용
#     return list(map(lambda x: x * 3, numbers))

# # 테스트
# input_list = [1, 2, 3, 4, 5]
# output = multiply_by_three(input_list)
# print(output)
