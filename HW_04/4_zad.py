def num_list(num):
    list1 = []
    for e in range(num):
        element = input("Enter a value for the list: ")
        if element.isnumeric():
            list1.append(int(element))
    return list1


def sum_list(list):
    sum = 0
    for k in list:
        if type(k) == float or type(k) == int or k.isnumeric():
            elem = float(k)
            sum += elem
    return sum


def max_of_two(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            if a >= b:
                return a
            else:
                return b
        return a
    elif type(b) == int or type(b) == float:
        return b
    elif type(a) != int or type(a) != float and type(b) != int or type(b) != float:
        return


print(max_of_two(sum_list(num_list(4)), sum_list(num_list(3))))
print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
