'''
mutable - 메모리 값을 변경 가능 객체(id 주소 안바뀜)
list, set, dict
'''
me = [1,2,3]
print(id(me))
me.append(4)
print(id(me))

'''
mutable - 메모리 값 변경 불가(id 주소 바뀜)
 정수(int), 실수(float), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me))
me += 1 # me = me +1
print(id(me))