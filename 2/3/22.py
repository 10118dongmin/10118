print_menu()
drink_key = select_drink()
if drink_key != -1:
    buy_drink(drink_key)

def select_drink():
    global inventory

    drink = int(input("메뉴를 선택하세요"))

    if drink == 1:
        drink_key = 'coke'
       # inventory.update({'coke': inventory['coke'] + 1})
    elif drink == 2:
        inventory['chill sung'] = inventory['chill sung'] + 1
    elif drink == 3:
        inventory['chocolate milk'] = inventory['chocolate milk'] + 1
    elif drink == 4:
        inventory['strewberry milk'] = inventory['strewberry milk'] + 1
    elif drink == 5:
        inventory['banana milk'] = inventory['banana milk'] + 1


    if inventory[drink_key] == 0:
        print("선택한 음료의 수량이 부족합니다.")
        return -1
    else:
        inventory[drink_key] =inventory[drink_key] -1
        return drink_key


    def buy_drink(drink_key: int):
        coin = 0
        while price[drink_key] > coin:
            print("금액을 입력하세요")
            coin = coin + int(input(">>"))

        print(coin - price[drink_key], "원을 반환합니다")


