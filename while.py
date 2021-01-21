# while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회.".format(customer, index))
#     index += 1
    
customer = "토르"
person = "Unknown"

# while person != customer: # True 가 될때까지 while 문 반복
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("고객이 누구입니까?")
    
# Continue / Break

absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1 ~ 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))