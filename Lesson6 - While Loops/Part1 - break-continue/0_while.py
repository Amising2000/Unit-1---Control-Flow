# Syntax
"""
initialize variable
while condition (test variable):
    code block
    increment/decrement variable
"""

num = 5
while num > 0:
    print(num)
    num -= 1


sum = 0
while num <= 10:
    sum += num
    num += 1

print(f"1+2+3+4+5+6+7+8+9+10 = {sum}")


# while num <= 10:
#     sum += num
#     if num < 10:
#         print(num, end='+')
#     else:
#         print(num, end='=')
#     num += 1
# print(sum)
# print()


# Sum of digits
# take a user input as int, and sum then digit it

# number = input("Enter a number: ")
sum = 0

# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Total {sum}")

# i = 0
# while i < len(number):
#     sum += int(number[i])
#     i += 1

# print(f"Total {sum}")


# Algorithm - sum of digits (as ints)
# n = int(input("Enter a number: "))
# number = n
# sum = 0
# while number > 0:
#     digit = number % 10 # get last digit
#     sum += digit # add to sum
#     number = number // 10 # remove last digit

# print(f"The sum of digits {n}: {sum}")



# Algorithm = count digits (as ints)
number = 54321
n = number
count = 0

while n > 0:
    count += 1
    n = n // 10

print(f"There are {count} characters in {number}")


