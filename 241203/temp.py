# # a = [[1, 2, 3],
# #      [11, 22, 33],
# #      ['leehojun', 20, 30]]

# # print(a[2][0][:3]) #슬라이싱 -> 012까지 출력

# # #기본적인 built-in functions
# # #1차원
# # a = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(max(a)) #최댓값
# # min(a) #최솟값
# # sum(a) #전체값의 합

# # #2차원
# # a = [[1, 2, 3],
# #      [11, 22, 33],
# #      [10, 2000, 30]]
# # print(max(a))
# # print(min(a))
# # print(sum(a))
# # max(a, key=lambda x:x[1])
# # min(a, key=lambda x:x[1])
# # # sum(a) error
# # sum(a, [])

# #2차원
# a = [[1, 2, 3],
#      [11, 22, 33],
#      [13, 20000, 300000]]

# for i in a:
#     print(i)

# #요소별로 순회하기
# # for i in a:
# #     for j in i:
# #         print(j)

# print(list(range(100)))
# # print(list(range(5, 10)))

# # #print(list(range(start, stop, step)))
# # print(list(range(0, 101, 2))) #짝수
# # print(list(range(1, 101, 2))) #홀수

# # print(list(range(100, 1, -2)))

# # print(list(range(5, 101, 5)))

# # print(list(range(-1, -100, -2)))






# # a = [i for i in range(1, 100) if i %3 == 0 or i %5 ==0]
# # print(a)


# # a = [i for i in range(-1, -101, -1)]
# # print(a)


# def f(a, b):
#     return dict.fromkeys(a, b)
# keys = ['A', 'B', 'C']
# value = 10
# s = f(keys, value)

# print(s)



# def make_dict(a,b)
#     return dict.fromkeys()





student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}

# - 학생들의 **총점**을 구하는 코드를 작성하세요.
# - 학생들의 **평균 점수**를 구하는 코드를 작성하세요.
# - 점수가 가장 **높은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.
# - 점수가 가장 **낮은** 학생의 이름과 그 점수를 구하는 코드를 작성하세요.

# total sum

# 총점 계산
total_score = sum(student_score.values())

# 출력
print(f"총점: {total_score}")


print(max(student_score))
print(min(student_score))