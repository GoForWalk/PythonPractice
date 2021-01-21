# class

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "marine"
# hp = 40
# damage = 5

# print("{} 유닛이 생성 되었습니다.".format(name))
# print("hp : {0}, damage : {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크 , 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성 되었습니다.".format(tank_name))
# print("hp : {0}, damage : {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# class 선언
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("hp : {0}, damage : {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40 ,5)
marine2 = Unit("마린", 40 ,5)
tank = Unit("탱크", 150, 35)
print()
# __init__ : python 에서 사용되는 생성자
# 객체가 생성 될때 자동적으로 호출되는 부분
# 객체 : class 로 부터 만들어지는 것
# marine / tank 는 Unit class 의 instance

# class 는 parameter를 일정하게 넘겨야 사용이 가능하다.

# 멤버 변수
# 클래스 내에서 정의된 변수
# self.~

wraith1 = Unit("레이스", 80, 5)
print("name: {0}, damage: {1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# clocking 이라는 변수는 class 에 선언하지 않았습니다.
# 파이썬에서는 class 선언부 밖에서도 변수를 추가로 할당할 수 있다.