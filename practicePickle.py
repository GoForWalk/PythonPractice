import pickle

# profile_file = open("profile.pickle", "wb") # w : write, b : binary
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)

# # profile 에 있는 정보를 file 에 저장
# pickle.dump(profile, profile_file)
# profile_file.close()


profile_file = open("profile.pickle", "rb") # r : read, b : binary
profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
