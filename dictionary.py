# key - value (Map 과 같다.)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 5라는 키가 존재 하지 않아서 오류발생
# print("hi")

print(cabinet.get(5)) # 키가 없으면 'none'을 리턴
print("hi")

# 해당 key 가 없는 경우 'none' 대신에 '사용 가능' 리턴
print(cabinet.get(5, "사용 가능"))
print("hi")

# dictionary 안에 키가 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

# -------------------------
cabinet = {"A-3" : "유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새손님
cabinet["C-20"] = "조세호"
print(cabinet)

# 유재석 -> 김종국
cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님 : del 사용
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())
# values들만 출력
print(cabinet.values())
# key, values들만 출력
print(cabinet.items())

#clear : dictionary 모두 지우기
cabinet.clear()
print(cabinet)
