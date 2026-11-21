account_A = 100000
account_B = 50000

amount = int(input('이체할 금액을 입력하세요: '))
if account_A > 0 and amount<=account_A:
    account_A = account_A - amount
    account_B = account_B + amount
else: print('이체 실패 !')

print('A계좌의 현재 잔액은' + str(account_A) + '원 입니다.')
print('B계좌의 현재 잔액은' + str(account_B) + '원 입니다.')


