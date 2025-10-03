# The continue statement
'''
**continue** - Skip to the next iteratiion
**Difference from break:**
- **break** -> exit the loop completely
- **continue** -> Skip the current interation, keep looping
'''

# Example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)