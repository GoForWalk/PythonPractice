# rasie 로 의도적으로 에러 발생시키기

# 에러를 직접 정의 하는 방법

class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except BigNumberError as err:
        print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
        print(err)

# finally : 오류발생 유무에 상관없이 무조건 발생하는 구문
finally: 
    print("계산기를 이용해 주셔서 감사합니다.")



