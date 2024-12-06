# 숫자 = [1, 2, 3, 4, 5]
# 승수 = [2, 2, 2, 3, 3]
# # 1.
# li = list(zip(숫자, 승수))


# def test(x):
#     return x >= 100

# def test1(x: tuple):
#     return x[0] ** x[1]


# a = list(map(test1, li))
# print(a)
# b = list(filter(test,a))
# print(b)


"""
문제: 학생들의 시험 점수가 담긴 딕셔너리를 점수에 따라 정렬하세요.
sorted() 함수와 람다 함수를 함께 사용해야 합니다.

요구사항:
1. sorted() 함수를 사용하세요
2. 람다 함수를 key 매개변수로 사용하세요
3. 점수가 높은 순서대로 정렬하세요(내림차순)
4. 결과는 [(학생이름, 점수)] 형태의 리스트여야 합니다

예시:
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
결과: [('David', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]

힌트:
- sorted()의 key 매개변수는 정렬 기준을 지정합니다
- 딕셔너리의 .items() 메서드를 사용하면 (키, 값) 쌍을 얻을 수 있습니다
- reverse=True 매개변수로 내림차순 정렬이 가능합니다
"""

### 1.2.11 sort

리스트를 정렬시켜주는 메서드입니다. 리스트의 역정렬을 하고 싶으면 sort를 한 뒤 reverse를 사용해주면 되겠죠?
a.sort()
a

a = [1, 2, 3, 4, 5, 1, 2]

b = sorted(a) # 오름차순 정렬 (Default)
print(b)

c = sorted(a,reverse=True) # 내림차순 정렬
print(c)


-> [1, 1, 2, 2, 3, 4, 5]


scores = ("alice:85, "bob:92")
sorted_scores = sort(scores)


# 학생들의 시험 점수가 담긴 딕셔너리
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

# sorted()와 람다 함수로 점수에 따라 내림차순 정렬
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# 결과 출력
print(sorted_scores)

scores = {}