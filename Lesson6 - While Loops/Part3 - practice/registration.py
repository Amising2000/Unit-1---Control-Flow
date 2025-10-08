while True:
    username = input("Enter a username (3-15 characters): ")
    
    if len(username) < 3:
        print("Too short! Min 3 characters")
        continue
    
    if len(username) > 15:
        print("Too long! Max 15 characters")
        continue
    
    has_space = False
    for char in username:
        if char == ' ':
            has_space = True
            
    if has_space:
        print("No spaces allowed")
        continue
    
    print(f"Username '{username}' accepted\n")
    break

while True:
    password = input("Enter a password (8+ characters): ")
    
    if len(password) < 8:
        print("Too short! Min 8 characters")
        continue
    
    has_digit = False
    has_space = False
    
    for char in password:
        
        if "0" <= char <= "9":
            has_digit = True
            
        if char == ' ':
            has_space = True

    if has_space:
        print("No spaces allowed")
        continue
    
    if has_digit == False:
        print("Password must have a digit")
        continue
    
    print(f"Password '{password}' accepted\n")
    break

while True:
    age = input("Please enter your age: ")
    
    if not age.isdigit():
        print("Please enter a valid number")
        continue
    
    age_int = int(age)
    
    if age_int < 13:
        print("Must be 13+ to register")
        continue
   
    if age_int > 120:
        print("Please enter a valid age")
        continue
    
    print(f"Age '{age_int}' accepted\n")
    break

while True:
    final = input("Would you like to register? (Yes, No, Y, N): ")
    final_lower = final.lower()

    if final_lower == "yes" or final_lower == "y":
        print("Registration successful")
        break
    elif final_lower == "no" or final_lower == "n":
        print("Registration canceled")
        break
    else:
        print("Please state either yes or no")
        continue