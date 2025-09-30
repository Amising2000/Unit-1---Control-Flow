# 1
password = input("Enter a password: ")

# 2
length = len(password)
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# 3
for char in password:
    if 'A' <= char <= 'Z':
        upper_count += 1
    elif 'a' <= char <= 'z':
        lower_count += 1
    elif '0' <= char <= '9':
        digit_count += 1
    elif not char == " ":
        special_count += 1

len_verify = length >= 8
upper_count_verify = upper_count >= 1
lower_count_verify = lower_count >= 1
digit_count_verify = digit_count >= 1
special_count_verify = special_count >= 1

# 4
repeat = False
repeat_text = ""
for i in range(len(password) - 2):
    if password[i] == password[i+1] == password[i+2]:
        repeat_text = f"Found 3 in a row: {password[i]}"
        repeat = True
        
simple = False
simple_text = ""
for i in range(len(password) - 2):
    if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
        simple_text = f"Found sequence: {password[i:i+3]}"
        simple = True
        
# Final
print(f"\nAnalyzing: ")
print("=" * 40)

print(f"Password: {password}")

print(f"\nCharacter Counts: ")
print(f"Length: {length} characters")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")

print(f"\nRequirement check: ")
print(f"{'✓' if len_verify else '⚠'} Length (8+ characters): {"Passed" if len_verify else "Failed"}")
print(f"{'✓' if upper_count_verify else '⚠'} Uppercase Letters: {"Passed" if upper_count_verify else "Failed"}")
print(f"{'✓' if lower_count_verify else '⚠'} Lowercase Letters: {"Passed" if lower_count_verify else "Failed"}")
print(f"{'✓' if digit_count_verify else '⚠'} Digits: {"Passed" if digit_count_verify else "Failed"}")
print(f"{'✓' if special_count_verify else '⚠'} Special Characters: {"Passed" if special_count_verify else "Failed"}")

print(f"\nSecurity Issues: ")

if repeat == False:
    print("✓ No repeated characters (3+)")
else:
    print(f"⚠ Repeated characters ({repeat_text})")
    
if simple == False:
    print("✓ No simple sequences (3+)")
else:
    print(f"⚠ Simple sequences ({simple_text}) found")

# 5
if len_verify and upper_count_verify and lower_count_verify and digit_count_verify and special_count_verify and repeat == False and simple == False:
    rating = "Strong"
elif len_verify and upper_count_verify and lower_count_verify and digit_count_verify and special_count_verify:
    rating = "Medium"
else:
    rating = "Weak"
    
print(f"Final Rating: {rating}")