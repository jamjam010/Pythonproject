'''
메소드(method)
특정 객체가 가지고 있는 함수
객체.메소드() 이 방식으로 사용
'''
# String 객체 format 메소드
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*>10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목이 짧은 기린 그림이다'
result = s.count('기린')
print(result)

# 5번째 인덱스부터 찾는다
s = 'best of best'
result = s.count('best', 5)
print(result)
s = 'best of best'
result = s.find('best', -7)
print(result)

# find() 메소드 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)

# 없는 값 find는 -1
result = s.find('z')
print(result)

s = 'apple'
result = s.index('p')
print(result)

# index() - find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러 발생
'''
s = 'apple'
result = s.index('z')
print(result)
'''