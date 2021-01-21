# 전역변수와 지역변수
gun = 10;

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 수 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감.
print("남은 총 : {0}".format(gun))

# parameter로 넣고 return 으로 값을 띄우는 것이 권장됨.
# global을 사용하게 되면 변수 활용이 어려워 코드에 바람직 하지 않다.

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers # 여기서 gun 은 지역번수
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 수 : {0}".format(gun))
checkpoint_ret(gun,2) # 2명이 경계 근무 나감.

