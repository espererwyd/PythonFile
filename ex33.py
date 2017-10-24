i = 0
numbers = []
max_range = 6
increment = int(input("> Please input your ideal increment here: "))

# def append_numbers_to_list(i):
#     while i < 6:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#
#         i += increment
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")
#
# append_numbers_to_list(i)
#
# print("The numbers:")
#
# for n in numbers:
#     print(n)
#
# print("So the list is: ", numbers)

def apppend_numbers_to_list(i):
    for i in range(0, max_range):
        print(f"At the top i is: {i}")
        numbers.append(i)

        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

apppend_numbers_to_list(i)

print("The numbers:")

for i in numbers:
    print(i)

print("So the list is: ", numbers)

# A for-loop can only iterate (loop) over collections of things.
# A while-loop can do any kind of iteration (looping) you want.
