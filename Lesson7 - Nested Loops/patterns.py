rows = 5
# spaces = 4
# stars = 1

# for i in range(1, rows + 1):
#         print(f"{' ' * spaces} {"*" * stars}")
#         spaces -= 1
#         stars += 2
#         print()
        
# Teacher way
# step1: create an outer loop for the rows
for i in range(rows):
        # step2: print the spaces row-i-1
        for j in range(rows-i-1):
                print(" ", end="")
        # step3: print the stars 2*i+1
        for k in range(2*i+1):
                print("*", end="")
        # step4: print a new line
        print()