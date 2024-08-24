a=100
print(a)
a="경신고등학교"
print(a)
a=0.5
print(a)

# 입력한 값을 변수에 대입
# b = input("값을 입력하세요 :")
# print(b +"(이)가 입력되었습니다.")

b = "100"
c = int(b) + 100 # 형변환
print(c)

d = c
print("c의 값은 ", c)
print("d의 값은 ", d)
c = 100
print("c의 값은 ", c)
print("d의 값은 ", d)

e = [100, 96, 87, 100]
f = e
print(e)
print(f)
e.append(95)
print(e)
print(f)