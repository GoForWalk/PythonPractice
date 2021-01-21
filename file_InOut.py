# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w : write
# print("Math : 0", file=score_file)
# print("English : 50", file=score_file)
# score_file.close() # 파일 닫기

# score_file = open("score.txt", "a" ,encoding="utf8") # a : append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽어오기
score_file = open("score.txt", "r" ,encoding="utf8") # r : read
print(score_file.read())
score_file.close()
# 모든 줄을 한번에 읽어 온다.

# # 줄 마다 따로따로 읽어오는 방법
# score_file = open("score.txt", "r" ,encoding="utf8") # r : read
# print(score_file.readline(), end="") # 줄별로 읽기ㅡ 한줄로 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 
# score_file.close()

# while 을 사용하여 파일을 line 마다 읽어오기
score_file = open("score.txt", "r" ,encoding="utf8") # r : read
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# list 를 사용하여 파일의 텍스트를 불러오는 방법
score_file = open("score.txt", "r" ,encoding="utf8") # r : read
lines = score_file.readlines() # 모든 line을 list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()
