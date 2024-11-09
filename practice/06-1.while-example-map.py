user_input = ""
X = 0
Y = 0

valid_inputs = ["EXIT", "UP", "DOWN", "LEFT","RIGHT"]

while user_input != "EXIT":
    user_input = ""  # user_input 초기화
    while user_input not in valid_inputs:
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

    if user_input == "UP":
        if Y < 100:
            Y = Y+1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input == "DOWN":
        if Y > 0:
            Y = Y-1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input =="LEFT":
        if X>0:
            X = X-1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input == "RIGHT":
        if X < 100:
            X = X+1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    print("현재 위치 : (",X,",",Y,")" )
print("프로그램을 종료합니다.")