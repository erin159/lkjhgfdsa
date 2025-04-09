# First name and age 
first_name =input("What is your name? ")
age = int(input("How old are you? "))
#if age is between 12 and 17 you can do it but if younger or older then that you are too older or young to do it
if age < 12:
    print("Sorry you must be 12 or older")
if age > 17:
    print("Sorry you must be 17 or younger")

# Choosing a activity to do 
options_activity = ["Music Jam Session (2 hours, easy, $5 fee)"," Science Experiments Lab (3 hours, moderate, $10 fee)", "Sport Leadership Training (4 hours, challenging, $12 fee)"]
# Chooseing a activity 
print("Choose an activity")
print(f"1. {options_activity[0]}")
print(f"2. {options_activity[1]}")
print(f"3. {options_activity[2]}")
options_activity = int(input("Enter the number of your chosen actvity:")) - 1
print("Choose an activity:")
if options_activity == 1:
    fee_activity = 5
elif options_activity == 2:
    fee_activity = 10
elif options_activity == 3:
    fee_activity = 12

if options_activity == 1:
    name_of_activity = (f"{options_activity[0]}")
elif options_activity == 2:
    name_of_activity = (f"{options_activity[1]}")
elif options_activity == 3:
    name_of_activity = (f"{options_activity[2]}")

# Chossing Meal options 
meal_option = ["Standard", "Vegetarian", "Dairy-free", "No Meal"]
print("Choose a Meal options")
print(f"1. {meal_option[0]}")
print(f"2. {meal_option[1]}")
print(f"3. {meal_option[2]}")
print(f"4. {meal_option[3]}")
meal_option = int(input("Enter the number of your choice meal"))
if meal_option == 1 or meal_option == 2 or meal_option == 3:
    food_fee = 7
elif meal_option == 4:
    food_fee = 0 

if meal_option == 1:
    name_of_meal = (f"{meal_option[0]}")
elif options_activity == 2:
    name_of_meal = (f"{meal_option[1]}")
elif options_activity == 3:
    name_of_meal = (f"{meal_option[2]}")

while True:
    final_question = input(f"Are you attending? (yes/no): ")
    final_question = final_question.lower ()
    if final_question == "yes" or final_question == "no" :
        break
    else: 
        print("Please enter yes or no")

print(f"your name is {first_name}, you are {age} years old, the activity you choose was {options_activity}, your meal option you choose was  {meal_option}. the total cost is ${food_fee + fee_activity}")