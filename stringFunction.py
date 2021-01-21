python = "Python is Amazing"

print(python.lower())
print(python.upper())

print(python[0].isupper())
print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n") # 첫번째 n
print(index)

index = python.index("n", index + 1) # 두번째 n
print(index)

print(python.find("n"))

print(python.find("Python")) # find : 찾고자 하는 문자열이 없는 경우 : -1 return
# print(python.index("Java")) # index : 찾고자 하는 문자열이 없는 경우 :  오류발생

print(python.count("n"))
