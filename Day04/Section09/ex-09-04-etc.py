'''
내장함수 보충
'''
result = format(10000) # str(10000)과 같다
print(type(result))
result = format(10000, ',') # 전단위 쉼표
print(result)

# abs() 절댓값
result = abs(10)
print(result)
result = abs(-10)
print(result)

# max() 최댓값 반환
# min() 최솟값 반환
result = max(1, 18)
print(result)
li = [5, 3, 4, 2, 1]
result = max(li)
print(result)

# pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 정렬 함수
my_li = [5, 6, 3, 4, 1, 2]
print(my_li)
result = sorted(my_li)
print(result)
print(result[0])
result = sorted(my_li, reverse=True)
print(result)

# zip()함수 - 같은 인덱스 번호끼리 튜플로 묶어줍니다
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]
for names, scores in zip(names, scores):
    print('{}의 점수는 {}입니다.'. format(names, scores))