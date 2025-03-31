# First name and age 
first_name =input("What is your name? ")
age =input("How old are you? ")

# Choosing a activity to do 
options_activity = ["Music Jam Session (2 hours, easy, $5 fee)"," Science Experiments Lab (3 hours, moderate, $10 fee)", "Sport Leadership Training (4 hours, challenging, $12 fee)"]
# Chooseing a activity 
print("Choose an activity")
print(f"1. {options_activity[0]}")
print(f"2. {options_activity[1]}")
print(f"3. {options_activity[2]}")
options_activity = int(input("Enter the number of your chosen actvity:"))

# Chossing Meal options 
meal_option = ["Standard", "Vegetarian", "Dairy-free", "No Meal"]
print("Choose a Meal options")
print(f"1. {meal_option[0]}")
print(f"2. {meal_option[1]}")
print(f"3. {meal_option[2]}")
print(f"4. {meal_option[3]}")
meal_option = int(input("Enter the number of your choice meal"))

print(f"your name is {first_name}, you are {age} years old, the activity you choose was {options}, your meal option you choose was  {meal_option}")