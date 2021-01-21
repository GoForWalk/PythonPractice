# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t 주사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교, 같은 반, 같은 수업.

# 기본 값 사용
# 함수 사용시 age, main_lang 에 대한 parameter 값이 없는경우 기본값을 return
def profile(name, age=17, main_lang="파이썬"): 
    print("이름: {0}\t나이 : {1}\t 주사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")