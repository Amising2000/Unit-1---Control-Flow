age = int(input("Enter your age: "))
rating = str(input("Enter movie rating: "))
rating_values = "G", "PG", "PG-13", "R"

# if age:
#     if 0 < age:
#         if rating == "G":
#             print("Aproved, you can watch this movie!")
#         else:
#             print("Warning, not recommended for your age!")
#     elif 6 <= age:
#         if rating == "PG" or "G":
#             print("Aproved, you can watch this movie!")
#         else:
#             print("Warning, not recommended for your age!")
#     elif 13 <= age:
#         if rating == "PG-13" or "PG" or "G":
#             print("Aproved, you can watch this movie!")
#         else:
#             print("Warning, not recommended for your age!")
#     else:
#         if rating == "R" or "PG-13" or "PG" or "G":
#             print("Aproved, you can watch this movie!")
#         else:
#             print("Denied, must be 17+ for R rated movies!")
# else:
#     print("Please enter a valid age")
    
    
if age:
    if 0 < age and rating == "G":
            print("Aproved, you can watch this movie!")
    elif 6 <= age and rating == "PG" or "G":
            print("Aproved, you can watch this movie!")
    elif 13 <= age and rating == "PG-13" or "PG" or "G":
            print("Aproved, you can watch this movie!")
    elif rating == "R" or "PG-13" or "PG" or "G":
            print("Aproved, you can watch this movie!")
    else:
        print("Denied!")
else:
    print("Please enter a valid age")