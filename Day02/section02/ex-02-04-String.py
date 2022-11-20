'''
하나 이상 연속된 문자(character)들의 나열
파이썬에서 문자열 자료형은 큰따옴표(" ")
또는 작은따옴표(' ') 사이에 위치
'''
# 'Hello' 와 "Hello" 동일
print('Hello' == "Hello")

'''
변수에 문자열 할당
'''

a = "Hello"
print(a)
'''
여러줄 문자열
세개의 따옴표를 사용하여 변수에 여러줄 문자열 할달
'''
a = """피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도란, 피죤튜, 또가스
"""
b =  '''피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도란, 피죤튜, 또가스
'''
print(a)
print(b)

'''
문자열 배열
문자열 인덱싱(indexing)
  h   e   l   l   o <== 문자열
  0   1   2   3   4
 -5  -4  -3  -2  -1
'''

a = "hello"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[2] == a[-2])

'''
문자열 슬라이싱
슬라이스 구문을 사용하여 문자 범위를 반환할 수 있다
문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 클론으로 구분하여 지정한다
'''
b = "Hello, World"
   # 01234567891011
print(b[2:5])
# 2~4까지 출력
print(b[:5])
# 0~4까지 출력
print(b[2:])
# 2부터 끝까지 출력
print(b.upper())
# b 변수를 전부 대문자로 전환해서 출력
print(b.lower())
# b 변수를 전부 소문자로 전환해서 출력

# 문자열 바꾸기
print(b.replace("H", "J"))

# 문자 합치기
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# NoneType
d = None
print(type(d))