print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (low + high) / 2
print("Is you secret number ", ans, "?")
instruction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")


while instruction != 'c':
    if instruction == 'h':
        high = ans
        ans = int((high + low) / 2)

    elif instruction == 'l':
        low = ans
        ans = int((high + low) / 2)

    else:
        print("Sorry, I did not understand your input.")

    print("Is your secret number ", ans, "?")
    instruction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")


print("Game over. Your secret number was: ", ans)
