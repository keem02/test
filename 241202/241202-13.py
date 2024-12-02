# # 함수를 이용하여 계산기 프로그램을 만들어주세요. 6 mins

# def plus(num1, num2):
# 	#이곳을 채워주세요

# def minus(num1, num2):
# 	#이곳을 채워주세요

# def multiply(num1, num2):
# 	#이곳을 채워주세요

# def divide(num1, num2):
# 	#이곳을 채워주세요

# print(f'plus : {plus(10, 5)}')
# print(f'minus : {minus(10, 5)}')
# print(f'multiply : {multiply(10, 5)}')
# print(f'divide : {divide(10, 5)}')



def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')

   

    # x의 n제곱을 구하는 함수
    # 재귀함수를 이용하여 만들어야 하먀
    # x는 0이 아니다 (x, n > 1 )

        
# def a = f('(x // n)')
# if x, n == 0:
#     return 1

# a = 1


def power(x, n):
# 기저 조건  n이 1일 때
    if n == 0:
        return 1
    else:
# 재귀 호출 x * x^
        return x * power(x, n-1)
    

# print(pow(2,3))

# a = [1, 2, 3]
# a + a
# a + 3
# a + [1]
# a - a
# a - [1]
# a / 3
# a // a
# a * a
# a * 3
# a * [3]


# 다음은 python 강좌 학생들의 시험 점수를 딕셔너리로 나타낸 것입니다.

student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}


#학생들의 총점을 구하는 코드를 작성하세요.
total_score = sum(student_score.values())
print(f'학생들의 총점은 {total_score}입니다.')

#학생들의 평균 점수를 구하는 코드를 작성하세요.
average_score = sum(student_score.values()) / len(student_score)
print(f'학생들의 평균 점수는 {average_score}입니다.')

#점수가 가장 높은 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
max_name = max(student_score, key=student_score.get)
max_score = student_score[max_name]
print(f'점수가 가장 높은 학생은 {max_name}이며, 그 점수는 {max_score}점입니다.')

#점수가 가장 낮은 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
min_name = min(student_score, key=student_score.get)
min_score = student_score[min_name]
print(f'점수가 가장 낮은 학생은 {min_name}이며, 그 점수는 {min_score}점입니다.')