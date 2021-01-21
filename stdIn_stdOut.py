# sep(seperate) 의 설정으로 값들 사이 연결 문장/ 형식을 설정 할 수 있다.
print("Python", "Java", sep=",") 
print("Python", "Java", sep=" vs ")
print("Python", "Java", sep=" ")
print("Python", "Java","JavaScript", sep=" | ")


# end 의 설정으로, 문장의 끝 부분을 설정 할 수 있다. 기본값으로 "\n" 설정되어 있다.
# end 의 설정을 바꾸면 print() 사이에 줄바꿈이 되지 않는다.
print("Python", "Java", sep=",", end="?")
print("Which one is more interesting?")


# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러 : Logging 기능
 
scores = {"Math":0, "English":50, "Coding":100}
for subject, score in scores.items(): # Key - Value pair
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # .ljust(8) : 8칸을 확보하고 왼쪽으로 정렬 / .rjust(4) : 4칸을 확보하고 오른쪽으로 정렬

# 은행 대기 순번표
# 001, 002, 003, ...

for number in range(1,12):
    # .zfill(3) : 3칸을 확보하고 나머지 공간으로 0 으로 채움
    print("대기번호 : " + str(number).zfill(3))

# input 으로 넣은 값은 String 형태로 return 된다.
answer = input("아무값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

