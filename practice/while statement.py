
# 수학 성적이 비정상적인 입력인 경우 다시 입력을 받는다
num = -1


while num > 100 or num < 0:
      num = int(input("수학 성적을 입력해주세요. ::"))

if   num > 80:
    print("A반입니다.")
elif num > 60:
    print("B반입니다.")
else:
    print("C반입니다.")

""" 
    
# up/down
# value = 10
# answer = 50
# down
# answer = 5
# up
import random
value = random.randrange(1,100)
print(value)

# 100 미만의 피보나치 수열 출력하기

# 사용자에게 숫자 하나를 입력받아서
# 해당 횟수만큼 * 출력하기 (별 출력)

# (0,0) 시작
# 사용자가 UP 입력하면 위로, DOWN 입력하면 아래로, LEFT 입력하면 왼쪽으로, RIGHT 입력하면 오른쪽으로
# MAP의 범위는 (0,0)~(100,100)
# (0,0) 가장 왼쪽의 아래, (100,100) 가장 오른쪽의 위
# 1. 잘못입력하면 처리x
# 2. 맵 밖에 못나가게 처리 (0,0) 에서 아래 누르면 잘못된 방향이라고 알려주고 (0,0) 유지
# EXIT 입력하면 종료

count = int(input("숫자 하나를 입력해주세요"))

i=0
stars = ""
while i < count:
    stars = stars + "*"
    i = i + 1
print(stars)