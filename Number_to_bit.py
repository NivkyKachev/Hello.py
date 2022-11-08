print("Enter a number:")
num = int(input())

print("Enter bit:")
bit = int(input())

str = ""

while num > 0:
    if num % 2 == 1:
        str += "1"
    else:
        str += "0"
    num = num // 2

print("The number in binary number system is:")
print(str[::-1])

if str[::-1][bit -1] == "1":
    print("1")
else:
    print("0")
