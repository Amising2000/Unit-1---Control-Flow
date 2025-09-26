# String indexing

word = "Python"
#       012345 (Positive indexing)
word[0] # P (first character)
word[1] # y (second character)
word[5] # n (last character)
word[-1] # n (last character)
len(word) # length of the word
word[len(word)-1] # n las character


# String Slicing
word[0:3] # Pyt (Characters 0,1,2)
word[:3] # Pyt (Characters 0,1,2)
word[2:5] # tho (Characters 2,3,4)
word[2:6] # thon (Characters 2,3,4,5)
word[2:len(word)] # thon (Characters 2,3,4,5)
word[2:] # thon (Characters 2,3,4,5)
word[-3:] # hon (character -3,-2,-1 or 3,4,5)


# Part1 - String Iteration Patterens

# Direct Character Iteration
word = "Hello"

for char in word:
    print(char)
    
    
# Index based iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")
    

# Character Classification
# char = 'A'
char = input("Press a key:")
# Check character types using ASCII ranges
if 'A' <= char <= 'Z':
    print(f"'{char}' is uppercase")
if 'a' <= char <= 'z':
    print(f"'{char}' is lowercase")
if '0' <= char <= '9':
    print(f"'{char}' is a digit")

if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    print(f"'{char}' is a letter")