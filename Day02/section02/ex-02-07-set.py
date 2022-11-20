'''
Set
순서가 없다
변경할 수 없다
인덱싱되지 않는 컬렉션
'''
thisset = {"피카츄", "라이츄", "파이리"}
print(thisset)
# 실행할 때 마다 순서 변경
for x in thisset:
    print(x)

# 값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)
# in은 앞에 값이 뒤에 값 안에 있는지 확인해줌

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 Set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)
# 중복 값은 추가 안됨 순서가 없기 때문

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# 없는 값을 제거하면 에러남

# 에러 안나는 항목 제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)

# 항목제거 무작위
thisset = {"피카츄", "라이츄", "파이리"}
thisset.pop()
print(thisset)

# 비우기
thisset.clear()
