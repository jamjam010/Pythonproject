'''
enumerate()
List, tuple, String 등 자료형을 입력받으면 인덱스 값을 포함하는 enumerate 객체를 돌려준다
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(type(enumerate(months)))
for months, day in enumerate(months):
    print('{}월 = {}일'.format(months+1, day))