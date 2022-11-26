'''
Casting
변수에 유형을 지정하려는 경우 캐스팅으로 가능
'''
# 정수형
x = int(1)
print(x)
y = int(2.8)#.8 소실, 정수만 입력
print(y)
z = int("3")
print(z)
print(type(z))
print(x + y + z)

# 실수형
x = float(1)
print(x)
z = float("3")
print(z)

#문자형
x = str(1)
y = str(2)
print(x)
print(y)
print(x + y)#문자이기 때문에 3이 아닌 12

#아스키 코드 변환
a = ord('A')
b = chr(65)
print(a)
print(b)