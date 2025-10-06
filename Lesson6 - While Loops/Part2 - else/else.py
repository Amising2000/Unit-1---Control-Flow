# while ... else
'''
The else clause runs when:
The loop completes normally
Without hitting a break
'''

# Basic example
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed")
    
# Basic example 2
count = 1
while count <= 5:
    if count == 3:
        break
    count += 1
else:
    print("This won't print")