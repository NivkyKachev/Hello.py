n = int(input("Въведи число: "))

s = []
for i in range(n):
    s.append(int(input("Въведи число за списъка: ")))
print(s)

num_two = int(input("Въведи 0 или 1: "))
if num_two == 0:
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] += 5

elif num_two == 1:
    for i in range(len(s)):
        if i % 2 != 0:
            s[i] += 10

print(s)
