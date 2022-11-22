num = int(input("Въведи число: "))

s = list()
for i in range(num):
    s.append(int(input("Въведи число за списъка: ")))
print(s)

num_two = int(input("Въведи 0 или 1: "))
if num_two == 1:
    for i in s:
        if i % 2 != 0:
            s = [i+10]
            # Прибавя 10 на нечетните числа от списъка и ги принтира.
            print(s, end=" ")

elif num_two == 0:
    for i in s:
        if i % 2 == 0:
            s = [i+5]
            # Прибавя 5 на четните числа от списъка и ги принтира.
            print(s, end=" ")
