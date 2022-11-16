n = int(input())
ser = n
sum = 0

for i in range(0, n):
    print(ser, end="+")
    sum += ser
    ser = ser * 10 + n

print(" =", sum)
