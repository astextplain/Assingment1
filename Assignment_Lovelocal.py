# Easy 1
def last_string(string1):
    splitted_string = string1.split()
    print(splitted_string)
    if len(splitted_string) == 0:
        return 0
    else:
        print("Length of the last element of the string", len(splitted_string[-1]))


input_string = input("Enter a string:")

last_string(input_string)


# Medium 1
def count_element(list1):
    if not list1:
        raise ValueError("Empty List")
    n = len(list1)
    dict1 = {}
    for i in list1:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    print(dict1)
    result = [key for key, value in dict1.items() if value > n // 3]
    print(result)


input_list = [3, 2, 3, 3, 3]
count_element(input_list)
# taking input from user
# input_list=[]
# input1=int(input("Enter the lenghth of the list"))
# for i in range(input1):
# num=input("Enter the element")
# input_list.append(num)
# print(input_list)


# Difficult 1


def palidrome_string(str1):
    reversed_string = str1[::-1]

    print(reversed_string)
    for i in range(len(str1) + 1):
        if str1.startswith(reversed_string[i:]):
            return reversed_string[:i] + str1


input_string = "fabcff"
print(palidrome_string(input_string))
