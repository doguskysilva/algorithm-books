MIN_SIZE_LIST = 0
MAX_SIZE_LIST = 99

size_list = int(input("Size of list: "))
list_numbers = []
result = 0
average = 0
sum = 0

if size_list > 0 and size_list < 100:
    for counter in range(0, size_list):
        list_numbers.append(int(input("Put a number: ")))
        sum = sum + list_numbers[counter]

    average = sum / size_list

    for counter in range(0, size_list):
        if list_numbers[counter] > average:
            result = result + 1

    print(f"The numbers above the average is {result}")
else:
    print("Lengh to list is not legal")
