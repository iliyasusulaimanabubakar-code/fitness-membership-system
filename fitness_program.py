
  
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

# Medical clearance check
has_condition = input(
    "Do you have a medical condition? (yes/no): "
).strip().lower()

if has_condition != "yes" and has_condition != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")

elif age >= 40 and has_condition == "yes":
    print("Medical clearance required before joining.")
    print("Please complete the clearance process first.")

else:
    print("You can proceed with registration.")

    # Membership plan selection
    membership = input(
        "Choose Basic or Premium: "
    ).strip().lower()

    if membership == "basic":

        personal_training = input(
            "Do you want personal training? (yes/no): "
        ).strip().lower()

        if personal_training == "yes":
            monthly_fee = 45

        elif personal_training == "no":
            monthly_fee = 30
            print("Consider upgrading to Premium for more benefits!")

        else:
            monthly_fee = None
            print("Invalid personal training choice.")

        if monthly_fee is not None:
            print("Monthly fee: $", monthly_fee)

    elif membership == "premium":

        monthly_fee = 60

        if age < 30:
            monthly_fee = monthly_fee * 0.90
            print("A 10% youth discount has been applied.")

        if has_condition == "yes":
            print("We recommend a free consultation before starting.")

        print("Monthly fee: $", monthly_fee)

    else:
        print("Invalid membership choice.")
  
