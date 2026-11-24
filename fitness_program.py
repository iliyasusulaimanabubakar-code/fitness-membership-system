# Fitness Membership Management System
# Beginner Python Portfolio Project

print("Welcome to Fitness Membership Management System")

# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello,", name)

# Check fitness program eligibility
if age < 18:
    print("You are eligible for the Teen Fitness Program.")
elif age <= 40:
    print("You are eligible for the Regular Fitness Program.")
else:
    print("You are eligible for the Senior Wellness Program.")
