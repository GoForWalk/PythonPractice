# 자료구조의 변경
# set
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

# list 로 변경
menu = list(menu)
print(menu, type(menu))

# tuple 로 변경
menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))