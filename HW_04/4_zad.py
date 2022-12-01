def Num_list():
    num = int(input("Enter how many numbers to add in the list: "))
    list1 = []
    for e in range(num):
        list1.append(input("Enter a value for the list: "))
    return list1


list_num = []
list_alphabet = []
list_second = Num_list()

for k in list_second:
    if k.isnumeric():
        list_num.append(k)
    else:
        if k.isalpha():
            list_alphabet.append(k)

print(list_num)
print(list_alphabet)

# Съжалявам, че не е цялата задача, но каквото и да мислех по нея все гърмеше и не успях да я направя както вие искате... :'(
# Наистина се опитвам да правя всичко по силите си, но... :"(
