# name and age 
first_name =input("what is your name")
age =input("how old are you")

# choose an activity from the list
options =["Music Jam Session (2 hours, easy, $5 fee)"," Science Experiments Lab (3 hours, moderate, $10 fee)", "Sport Leadership Training (4 hours, challenging, $12 fee)"]

# option list 
print("choose an activity")
print(f"1. {options[0]}")
print(f"2. {options[1]}")
print(f"3. {options[2]}")
options = int(input("Enter the number of your activity choice"))
# Meal option 
meal_option = ["Standard", "Vegetarian", "Dairy-free", "No meal"]

print("Chosse a Meal options")
print(f"1. {meal_option[0]}")
print(f"2. {meal_option[1]}")
print(f"3. {meal_option[2]}")
print(f"4. {meal_option[3]}")
meal_option = int(input("Enter the number of your choice meal"))

print(f"your name is {first_name}, you are {age} years old, the activity you choose was {options}, your meal option you choose was  {meal_option}")