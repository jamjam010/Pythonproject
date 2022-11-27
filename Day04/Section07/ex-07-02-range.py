'''
for 문과 range 함수
'''
# range(1, 10)은 1부터 9까지
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{}x{}={}'.format(dan, n, dan*n))

# range(10)은 0부터 9까지
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10, 3):
    print('{}x{}={}'.format(dan, n, dan*n))

# range(1, 10, 3) 1부터 9까지 2씩 증가
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10, 3):
    print('{}x{}={}'.format(dan, n, dan*n))
