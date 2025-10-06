# Break statements in loops
# break - Exit the loop immedistely
# use cases:
'''
*Stop when you find something
*Exit early based on conditions
*Get out of infinite loops
'''
count = 1
while count <= 10:
    print(count)
    if count == 5:
        break
    count += 1
    
while True:
    choice = input("Enter something: (q for quit): ")
    if choice == "q":
        print("You wanted to exit.")
        break
    print(f"You entered {choice}")
    

# Find first divisor
n = 15
divisor = 2

while divisor < n:
    if n % divisor == 0:
        break # Found
    divisor += 1
    
print(divisor)