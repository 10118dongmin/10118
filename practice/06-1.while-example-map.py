# 시작 위치
x, y = 0, 0


def move_player(direction):
    global x, y

    if direction == "up":
        if y < max_limit:
            y += 1
        else:
            print("잘못된 방향: 맵 밖으로 나갈 수 없습니다.")
    elif direction == "down":
        if y > min_limit:
            y -= 1
        else:
            print("잘못된 방향: 맵 밖으로 나갈 수 없습니다.")
    elif direction == "left":
        if x > min_limit:
            x -= 1
        else:
            print("잘못된 방향: 맵 밖으로 나갈 수 없습니다.")
    elif direction == "right":
        if x < max_limit:
            x += 1
        else:
            print("잘못된 방향: 맵 밖으로 나갈 수 없습니다.")
    else:
        print("잘못된 명령입니다. 'up', 'down', 'left', 'right' 중 하나를 입력하세요.")


