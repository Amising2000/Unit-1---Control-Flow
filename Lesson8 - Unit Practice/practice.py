n = 5
# n_input = input("Enter a number: ")
# if not n_input.isdigit():
#     print("Enter a valid number.")
# else:
#     n = int(n_input)

count = 0

for i in range(n):
    if i == n-1 or i == 0:
        print("X " * n)
    else:
        for j in range(n):
            if j == n-1 or j == 0:
                print("X ", end="")
            else:
                print("O ", end="")
                count += 1
        print()
        
count
print(f"Safe: {count}")

