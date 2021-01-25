class Byme():
    def __init__(self, name, youtube, email):
        self.name = name
        self.email = email
        self.youtube = youtube
    
    def sign(self):
        print("이 프로그램은 {0}에 의해 만들어졌습니다.".format(self.name))
        print("유튜브 : {0}".format(self.youtube))
        print("이메일 : {0}".format(self.email))