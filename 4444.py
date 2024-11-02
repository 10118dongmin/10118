"""
# 사용자에게 수학점수를 입력받아
# 상/중/하 반으로 분류 해주기
# 상 - 90점 이상인 사람
# 중 - 70점 이상인 사람
# 하 - 나머지

size = int(input("수학 시험 점수를 입력해주세요"))
print(size)

if size > 100 or size < 0:
    print("점수를 잘못입력하셨습니다.")
elif size >= 90:
    print("당신은 상반입니다.")
elif size >= 70:
    print("당신은 중반입니다.")
else:
    print("당신은 하반입니다.")

if size > 100 or size < 0:
    print("점수를 잘못입력하셨습니다.")
else:
    if size >= 90:
        print("당신은 상반입니다.")
    elif size >= 70:
        print("당신은 중반입니다.")
    else:
        print("당신은 하반입니다.")
"""

"""
# 예제 1번
# 사용자에게 숫자를 입력받아서 홀수면 "홀수입니다", 짝수면 "짝수입니다" (나머지 연산 %)

num = int(input("숫자를 하나 입력해주세요. ::"))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
"""
"""
# 예제 2번
# 사용자에게 문장 하나를 입력받아서 "파이썬" 이라는 글자로 시작하면 (str[:])
# "파이썬 관련된 얘기군요!" 라고 대답해주기

str = input("안녕하세요! 무슨 주제에 대해 말씀하고 싶으세요? :: ")
if str[:6] == "Python":
    print("파이썬 관련된 얘기군요!")
"""
"""

# 예제 3번
# 간단한 MBTI 게임 (if)
# "당신은 주말에 보통 무엇을 하며 시간을 보내나요?"
# 1. 집에서 쉬는 편이다- I
# 2. 친구들과 약속을 잡아 나가는 편이다 - E
# "갑자기 상공에 외계인이 나타난다면?"
# 1. 어쩌면 인간 친화적인 외계인일지도..?- N
# 2. 외계인이 왜 나타나냐 - S
# "슬픔을 둘로 나누면?"
# 1. 슬과 픔 - T
# 2. 슬픔이 덜어진다 - F
# "계획했던 식당이 갑자기 휴무면?"
# 1. 근처 아무 식당이나 간다 - P
# 2. 이미 Plan B가 있다 - J

MBTI = ""

print("당신은 주말에 보통 무엇을 하며 시간을 보내나요?")
print("1. 집에서 쉬는 편이다")
print("2. 친구들과 약속을 잡아 나가는 편이다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "I"
elif answer == 2:
    MBTI = MBTI + "E"

print("갑자기 상공에 외계인이 나타난다면?")
print("1. 어쩌면 인간 친화적인 외계인일지도..?")
print("2. 외계인이 왜 나타나냐")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "N"
elif answer == 2:
    MBTI = MBTI + "S"

print("슬픔을 둘로 나누면?")
print("1. 슬과 픔")
print("2. 슬픔이 덜어진다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "T"
elif answer == 2:
    MBTI = MBTI + "F"

print("계획했던 식당이 갑자기 휴무면?")
print("1. 근처 아무 식당이나 간다")
print("2. 이미 Plan B가 있다")

answer = int(input(">>"))
if answer == 1:
    MBTI = MBTI + "P"
elif answer == 2:
    MBTI = MBTI + "J"

print("당신의 MBTI는 -> ", MBTI)

"""
