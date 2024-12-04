# 함수를 만들되 두 가지의 인자를 받고
# 두 가지의 인자는 각각 문자열이다
# 두 가지의 인자에서 a라는 갯수를 세고
# 그 갯수를 조건문 if, else를 사용해서
# a의 갯수가 더 많으면 True
# b의 갯수가 더 많으면 False
# 같으면 -1을 리턴하라

# def compare_a_and_b_count(string1, string2):
#     # 각 문자열에서 'a'의 갯수 세기
#     count_a1 = string1.count('a')
#     count_a2 = string2.count('a')
    
#     # 조건에 따라 결과 반환
#     if count_a1 > count_a2:
#         return True
#     elif count_a1 < count_a2:
#         return False
#     else:
#         return -1

# 예제 실행
# result = compare_a_and_b_count("banana", "apple")
# print(result)  # 출력: -1

# def strings(apple, banana)
    
#     count = apple.count(a)
#     count = banana.count(a)



# 10:24 - 10:35 if문은 여기서 끝
"""
1. 함수를 만든다. 3개의 인자(문자열)을 받는다.
2. 각 인자의 길이를 변수 a, b, c에 저장한다.
3. if,elif,else문을 사용하여 
a,b,c의 길이가 같으면 "모두 같다", 
하나만 다르면 "하나만 다르다",
모두 다르면 "모두 다르다"를 출력한다.

"""

# def string(apple, banana, orange):
#     a = len(apple)
#     b = len(banana)
#     c = len(orange)

#     if a == b == c
#     print("모두 같다")
#     elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
#         print("하나만 다르다")
#     else:
#         print("모두 다르다")



# def compare_string_lengths(str1, str2, str3):
#     # 각 문자열의 길이를 변수에 저장
#     a = len(str1)
#     b = len(str2)
#     c = len(str3)
    
#     # 조건문을 사용해 결과 판단
#     if a == b == c:
#         print("모두 같다")
#     elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
#         print("하나만 다르다")
#     else:
#         print("모두 다르다")

# # 예제 실행
# compare_string_lengths("hello", "world", "hello")  # 출력: 하나만 다르다
# compare_string_lengths("abc", "def", "ghi")        # 출력: 모두 같다
# compare_string_lengths("abc", "def", "ghij")       # 출력: 모두 다르다


def string(a=apple, b=banana, c=orange):
    a = len(apple)
    b = len(banana)
    c = len(orange)

    if a == b == c:
        print("모두 같다")
    elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
        print("하나만 다르다")
    else:
        print("모두 다르다")