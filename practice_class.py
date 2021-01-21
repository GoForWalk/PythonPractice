class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __inti__(self):
        # super().__init__()        
        # 다중 상속을 받는 경우, super()를 사용하면 순서 상 먼저 상속받는 부모에 대한 __init__이 생성되므로,
        # 다중 상속의 경우 super() 사용보다, 부모 클래스의 명칭을 입력해주는 것이 더 정확하다. 
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

