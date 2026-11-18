accounts = {
    "A": 100000,
    "B": 50000,
    "C": 200000
}

while True:
    print("==Mini Bank==")
    print("1. 계좌 조회")
    print("0. 종료")

    a = int(input("메뉴 선택: "))

    if a == 1:
        x = input("조회할 계좌: ")
        if x == "A":
            print(accounts["A"])
        elif x == "B":
            print(accounts["B"])
        elif x == "C":
            print(accounts["C"])
        else:
            print("존재하지 않는 계좌입니다")
    if a == 0:
        print("프로그램을 종료합니다.")
        break




