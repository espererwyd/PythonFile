num = input("Enter a number here:> ")

result = ''

if float(num) < 0.0:
    isneg = True
elif float(num) == 0.0:
    print("0")
else:
    isneg = False


if '.' in num:
    num = abs(float(num))
    sq = 0
    while num % 1.0 != 0.0000:
        sq = sq + 1
        num = num * 2
    remainder1 = 0
    while int(num) > 0:
        remainder1 = int(num % 2)
        num = int((num - remainder1) / 2)
        result += str(remainder1)
    result = result[::-1]
    print("result before left shifting is", result, "and sq is ", sq)

    result = float(result)
    result /= (10 ** sq)
    result = str(result)

else:
    num = abs(int(num))
    remainder2 = 0
    while num > 0:
        remainder2 = int(num % 2)
        num = int((num - remainder2) / 2)
        result += str(remainder2)
    result = result[::-1]

if isneg == True:
    result = '-' + result
else:
    pass

print(result)
