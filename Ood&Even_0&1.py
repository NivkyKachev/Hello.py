num = int(input("Въведи число: "))
num_two = int(input("Въведи 0 или 1: "))

s = list(i for i in range(1, num+1))
print(s)

if num_two == 1:
    for n in s:
        if n % 2 != 0:
            s = [n+10]
            # Прибавя 10 на нечетните числа от списъка и ги принтира.
            print(s, end=" ")

elif num_two == 0:
    for i in s:
        if i % 2 == 0:
            s = [i+5]
            # Прибавя 5 на четните числа от списъка и ги принтира.
            print(s, end=" ")
