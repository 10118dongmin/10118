user_input = ""
X = 0
Y = 0

directions = ["UP", "DOWN", "LEFT","RIGHT"]
dx = [0,0,-1,1]
dy = [1, -1, 0,0]
valid_inputs = ["EXIT"]+directions

while user_input != "EXIT":
    user_input = ""  # user_input 초기화
    while user_input not in valid_inputs:
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

    if user_input in directions:
        index = directions.index(user_input)

        tmpX = X+dx[index]
        if tmpX > 10 or tmpX < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            X = tmpX

        tmpY = Y+dy[index]
        if tmpY > 10 or tmpY < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            Y = tmpY

    print("현재 위치 : (",X,",",Y,")" )

print("프로그램을 종료합니다.")


import random
alphabet = []

for i in range(0,10):
    alphabet.append(chr(random.randrange(65,91)))
#문제 1
# 사용자한테 숫자하나를 입력>
# 해당 숫자의 구구단을 출력
# 2 를 입력받으면
# 2*1=2 ~ 2*9=28

# 문제 2
# 10 개의 랜덤 알파벳을 배열로 생성
# [Q,W,A,F,S,C,G,D,E,T]
# 하나씩 출력되며, 사용자가 해당 알파벳을 빠르게 입력하는 게임
# 출력 : Q
# 사용자 입력 : Z  <- 넘어가지 않음
# 사용자 입력 : Q <- 다음문제인 W가 출력됨

import random
alphabet = []

for i in range(0,10):
    alphabet.append(chr(random.randrange(65,91)))



import random
alphabet = []

for i in range(0,10):
    alphabet.append(chr(random.randrange(65,91)))

for alpha in alphabet:
    print(alpha)
    while user_input != alpha:
        user_input = input("")