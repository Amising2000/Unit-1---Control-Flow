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

number = input("Enter a number: ")
sum = 0

# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Total {sum}")

i = 0
while i < len(number):
    sum += int(number[i])
    i += 1

print(f"Total {sum}")