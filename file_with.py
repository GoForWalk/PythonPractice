import pickle

# 변수 설정을 따로 해주지 않아도 사용가능하다. 
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# close() 를 사용하지 않아도 된다.

# pickle 파일 말고 일반 .txt 파일 로드
# with 구문 사용

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("studying Python")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


