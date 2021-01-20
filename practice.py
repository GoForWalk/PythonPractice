import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 주석
animal = "강아지"
name = "우리집"
age = 4
hobby = "산책"
is_adult = age >= 3

# + 를 사용하여 변수 연결
# boolean, int type을 string 형태로 사용하기 위해서 str(변수) 사용한다. 
print(name + animal + "True")
print("우리집" + str(age) +" True")
print(name + "우리집" + str(is_adult))

# , 를 사용하여 변수 연결 가능
# , 를 넣으면 띄어쓰기 발생
print(name + animal + "True")
print("우리집",str(age) ," True")
print(name,is_adult)

# 주석사용 방법

# 사용

# ''' 작은 따옴표 3개로 해당 주석 감싸기
''' 주석입니다.
주석입니다.
주석입니다.
주석입니다.'''
# 주석 단축키 : 컨트롤 + / 
