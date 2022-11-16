num = int(input())
factorial = 1

if num < 0:
    print("Не съществува факториел на отрицателни числа!")
elif num == 0:
    print("Факториел на 0 е 1")
else:
    for i in range(1, num + 1):

        factorial = factorial * i
    print("Факториел на", num, "е", factorial)
