i = 0
numbers = []
range_condition = (0,6)
increment = int(input("> Please input your ideal increment here: "))

def append_numbers_to_list(i):
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

append_numbers_to_list(i)

print("The numbers:")

for n in numbers:
    print(n)

print("So the list is: ", numbers)
