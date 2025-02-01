d = {"key":"value", 2.3: "value", 5:1, 5:"111"}
print(d)

print(d.keys())
print(d.values())

"""
# 자판기 프로그램을 할 것
# 사용자모드 / 관리자모드
# 사용자모드 - 물건 구매
# 관리자모드 - 물건 추가, 물건 가격 변동
inventory = {}
#사용자 모드

if not inventory :
    print("X")
elif inventory :
    answer = input("선택")
    if inventory.key == answer:
        print("O")
    else:
        print("X")

#관리자 모드
c = input("입력")


# 각각의 dictionary
inventory = {'coke':10, 'cider':5, 'choco-milk':3}
price = {'coke':800, 'cider':700, 'choco-milk':1000}

mode = "manager"

