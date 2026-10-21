#가상 은행 계좌 잔액
account_A = 100000
account_B = 50000

#이체할 금액
amount = 30000

#이체 가능 여부 확인
if amount > 0 and account_A >= amount:
    account_A = account_A - amount
    account_B = account_B + amount
    print('계좌이체 성공!')
else:
    print('이체 실패 !')

# 이체 후 잔액 출력
print('A계좌 잔액:', account_A)
print('B계자 잔액:', account_B)
