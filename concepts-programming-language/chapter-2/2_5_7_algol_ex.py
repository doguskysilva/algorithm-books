list_numbers = []
result = 0
average = 0
sum_list = 0
size_list = int(input("Size of list: "))

if size_list > 0 and size_list < 100:
    for counter in range(0, size_list):
        list_numbers.append(int(input("Put a number: ")))
        sum_list = sum_list + list_numbers[counter]

    average = sum_list / size_list

    for counter in range(0, size_list):
        if list_numbers[counter] > average:
            result = result + 1

    print(f"The numbers above the average is {result}")
else:
    print("Lengh to list is not legal")
