# 사용자에게 수학점수를 입력받아
# 상/중/하 반으로 분류 해주기
# 상 - 90점 이상인 사람
# 중 - 70점 이상인 사람
# 하 - 나머지

size = int(input("수학 시험 점수를 입력해주세요"))
print(size)

if size > 100 or size < 0:
     print("점수를 잘못입력하셨습니다.")
if size >= 90:
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
    elif size >=70:
        print("당신은 중반입니다.")
    else:
        print("당신은 하반입니다.")



    #예제 1번 사용자에게 숫자를 입력받아서 홀수면 "홀수입니다", 찍수면 "짝수입니다"
    number = int(input("숫자를 입력해주세요"))
    print(number)

    if number is ("odd number")
        print("홀수입니다")
    if number is ("even number")
        print("짝수입니다")