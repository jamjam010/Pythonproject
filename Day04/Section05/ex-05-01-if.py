'''
조건문
특정 조건을 만족하는지 여부에 따라 실행하는 코드가 달라야 할 때 사용한다
들여쓰기를 사용하여 코드의 범위 정의

1. 방법
if(조건식):
    실행할 코드

2. 방법
if(조건식):
    실행할 코드
else:
    실행할 코드

3. 방법
if(조건식1):
    실행할 코드
elif(조건식2):
    실행할 코드
else:
    실행할 코드
'''
#if(조건식)
a = 7
b = 100
if b > a:
    print("b는 a보다 크다")

#if(조건식) else
a = 7
b = 4
if b >= a:
    print("b는 a보다 크거나 같다")
else:
    print("b는 a보다 작다")

#if(조건식1) elif(조건식2) else
a = 20
b = 20
if b > a:
    print("b는 a보다 크다")
elif b == a:
    print("b는 a와 같다")
else:
    print("b는 a보다 작다")