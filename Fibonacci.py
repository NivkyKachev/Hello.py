num = 0
numinput = int(input())

print("Фибоначи:")

for i in range(10):
    print(num, end=" ")
    resul = num + numinput

    num = numinput
    numinput = resul
