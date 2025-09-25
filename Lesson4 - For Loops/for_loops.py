# Three formms of range() function
# range(stop)
for i in range(5): # 0,1,2,3,4
    print(i)
# range(start, stop)
for i in range(3,8): # 3,4,5,6,7
    print(i)
# range(start, stop, step)
for i in range(2,11,2): # 2,4,6,8,10
    print(i)
# Counting backwards
for i in range(10,1,-2): # 10,8,6,4,2
    print(i)
    
# Countdown Timer
import time
print('Countdown:')
for seconds in range(10,-1,-1):
    print(f"{seconds}")
    time.sleep(i)
print('BLAST OFF!🚀')

#Multiplication Table
# Take user input for the nuber and pring the table
# If the user submitted 5:
#   5x1=5
#   5x2=10
# numberx1=number

table = int(input("Give number:"))

if table:
    for i in range(1,13):
        print(f"{table} x {i}: {table * i}")
else:
    print("Enter a number vro")