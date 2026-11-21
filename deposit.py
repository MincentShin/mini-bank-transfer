accounts = {
    "A" : 100000,
    "B" : 50000,
    "C" : 200000
}

while True:
    print("==Mini Bank==")
    print("1. 계좌 조회")
    print("2. 계좌 입금")
    print("0. 종료")

    a = input('메뉴를 입력하세요: ')

    if a == '1':
        b = input('조회할 계좌를 입력하세요: ')

        if b in accounts:
            print(b, '계좌 잔액:', accounts[b], '원')
        else:
            print('존재하지 않는 계좌입니다.')
    elif a == '2':
        c = input('입금할 계좌를 입력하세요: ')

        if c in accounts:
            try:
                d = int(input('입금할 금액을 입력하세요: '))

                if d>0:
                    accounts[c] += d
                    print('입금이 완료되었습니다.')
                    print(c, '계좌 잔액: ', accounts[c], '원')
                else:
                    print('0원 또는 음수는 입금할 수 없습니다.')
            except ValueError:
                print('숫자만 입력해주세요.')
        else:
            print('존재하지 않는 계좌입니다.')
    elif a == '0':
        print('프로그램을 종료합니다.')
        break

    else:
        print('잘못된 메뉴입니다.')
    