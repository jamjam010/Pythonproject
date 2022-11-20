'''
List
단일 변수에 여러 항목을 저장하는데 사용된다
List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
List에는 다양한 데이터 유형이 포함될 수 있다
'''
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist)
print(thislist[0])
# list 길이
print(len(thislist))

# List 데이터 유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list2 = [1, 2, 3, 4]
list3 = [True, False, False]
# 다양한 유형 포함 가능
list4 = ["abc", 34, False, 40]

# 항목
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])

# 변경
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist[1] = "잠만보"
print(thislist)

# 여러값 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울머기", "메타몽"]
print(thislist)

# 항목추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)

# 인덱스 번호 자리에 항목추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)

# 항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove("라이츄")
print(thislist)

# 항목을 규정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)
print(thislist)

# 마지막 값만 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop()
print(thislist)

# 목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)

# 리스트 확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플", "야도란"])
print(thislist)

# 객체 삭제
del thislist
# print(thislist) 정의가 안되서 에러남
print("bbb")