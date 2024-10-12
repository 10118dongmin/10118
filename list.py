a = [100, 96, 87, 123, 1231, 31231, 31231]

print(a[0])
print(a[1])

print(a)
print(a[0:5]) #a[N:M] a 의 N번째 요소부터 M-1번째 요소까지
print(a[4:5])
print(a[3:])
print(a[:4])

b = [[1100, 87, 98, 99, 95], [75, 68, 100, 83, 88], [95, 75, 88, 79, 93]]

print(b[0][1])
print(b[1])
print(b[0][2:])
print(b[1:])

c = [[[100, 99, 98, 97 ,133], 87, 98, 99, 95], [75, 68, 100, 83, 88], [95, 75, 88, 79, 93]]

print("=======================")

d = [13, 12, 61, 23, 16]
e = d

d[1] = 10

print(d)
print(e)

f = a + d
print(f)

g = a + b
print(g)

h = d * 3
print(h)

print(len(a))
print(len(b))
print(len(b[0]))