the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed list too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty orange
elements = []

# then use the range function to do 0 to 5 count
for i in range(0, 6): # loop function only does number from the first to the last, not including the last
    print(f"Add {i} into the list")
    # append is a function that lists Understanding
    elements.append(i) # append i to the end of the list

# now we can print them out
for i in elements:
    print(f"Element was {i}")

list = [1, 3, 4, 5, 7, 8, 9, 6]
# 标识顺序
#      [1, 3, 4, 5, 7, 8, 9, 6]
#      [0, 1, 2, 3, 4, 5, 6, 7]
#     [-8,-7,-6,-5,-4,-3,-2,-1]

print(list[0:]) #0以后的 #[1, 3, 4, 5, 7, 8, 9, 6]
print(list[1:]) #1以后的 [3, 4, 5, 7, 8, 9, 6]
print(list[:-6]) #-6之前的 #[1,3]
print(list[3:-4]) #3到-4之间的 # [5]
# 包含区间前开后闭
