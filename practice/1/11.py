def warm_up():
    print("음료를 데웁니다.")


def add_ice():
    print("얼음을 넣습니다.")


def add_esspresso():
    print("espresso를 넣습니다.")


def add_water():
    print("물을 넣습니다.")


def add_milk():
    print("우유를 넣습니다.")


def add_cocoa():
    print("코코아를 넣습니다")



def make_drink(order):
    if order == "핫 에스프레소":
        print("에스프레소를 넣고 음료 완성!")
    elif order == "아이스 아메리카노":
        print("얼음을 넣고 -> 물을 넣고 -> 에스프레소를 넣으면 음료 완성!")
    elif order == "핫 모카라떼":
        print("우유를 넣고 -> 데우고 -> 에스프레소를 넣고 -> 코코아를 넣으면 음료 완성!")
    elif order == "아이스 라떼":
        print("얼음을 넣고 -> 우유를 넣고 -> 에스프레소를 넣으면 음료 완성!")
    elif order == "아이스 코코아":
        print("얼음을 넣고 -> 우유를 넣고 -> 코코아를 넣으면 음료 완성!")

