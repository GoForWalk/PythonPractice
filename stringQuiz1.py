import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호 : nav51!

'''

# url = "http://naver.com"
url = "http://google.com"

# httpindex = address.find("http://")
# httplength = len("http://")

# httpsize = httpindex + httplength

# address = address[httpsize:]

address = url.replace("http://", "")

# dotIndex = address.find(".")
# address = address[:dotIndex]
address = address[:address.find(".")]

numberE = address.count("e")
numberAddress = len(address)

password = address[:3]+str(numberAddress)+str(numberE)+"!"

print("{0} 의 비밀번호는 {1} 입니다." .format(url,password))