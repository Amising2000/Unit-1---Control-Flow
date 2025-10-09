rows = 5
spaces = 4
stars = 1

for i in range(1, rows + 1):
        print(f"{' ' * spaces} {"*" * stars}")
        spaces -= 1
        stars += 2
        print()