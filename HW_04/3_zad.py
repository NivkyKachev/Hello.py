def Average(list):
    return sum(list) / len(list)
    return sum(multiplied_list) / len(multiplied_list)


num = int(input("Enter how many numbers to add in the list: "))
list = []
list_multiplier = []

for i in range(num):
    list.append(float(input()))
print(list)

average = Average(list)
print("Average of the list =", round(average, 2))

copy_list = list
multiplied_list = []

for elements in copy_list:
    rounded_elements = round(elements)
    multiplied_list.append(rounded_elements * 2)
print(multiplied_list)

multiplied_average = Average(multiplied_list)
print("Average of the converted list =", round(multiplied_average, 2))
