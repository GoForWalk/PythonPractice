print("a" + "b")
print("a", "b")

# 방법 1 : % 사용
# 다양한 문자열 format 지정 방식
print("나는 %d살 입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." %"A")

# %s 를 사용하면 거의 모든 내용을 print 할 수 있다.
print("나는 %s살 입니다." % 20)

# 다양한 값 print
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법 2 : {} 사용
print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) # {} 안에 순서 부여
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3 
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age = 20))

# 방법 4 (파이썬 v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")