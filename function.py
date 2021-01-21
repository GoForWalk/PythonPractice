def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance, money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 현재 잔액 : {0}".format(balance))
        return balance

def withdraw_night(balence, money): # 저녁에 출금
    commission = 100 # 수수료 100원

    return commission, balance - money - commission # tuple type 으로 return
    

balance = 0
balance = deposit(balance , 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print("수수료는 {0}이며, 잔액은 {1} 원입니다.".format(commission, balance))
