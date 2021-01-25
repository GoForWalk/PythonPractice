class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행")

if __name__ == "__main__": # __name__ 이 __main__ 이면, 
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 시행핼 떄만 실행되요.")

    trip_to = ThailandPackage()
    trip_to.detail()
else: 
    print("Thailand 외부에서 모듈을 호출")