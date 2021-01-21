# keyword
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", age = 20, main_lang="파이썬")
# profile(main_lang= "java", name="kevin", age=30)

# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 줄바꿈이 되지 않는다.
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()


profile("Kevin", 20, "java", "python", "C", "C++", "C#", "JavaScript")
profile("Jason", 25, "Kotlin", "Swift",) 
