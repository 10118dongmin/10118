
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