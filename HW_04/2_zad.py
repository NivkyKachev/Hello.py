n = int(input("Enter a number: "))
dict1 = {}
for i in range(n):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    dict1[key] = value

m = int(input("Enter a number for the list: "))
list1 = []
for i in range(m):
    list1.append(input("Enter a value for the list: "))

second_list = []

for k in list1:
    element = k
    while k in dict1:
        element = dict1.get(k)
        del dict1[k]
    else:
        second_list.append(element)

print("Dictionary: ", dict1)
print("List: ", second_list)
