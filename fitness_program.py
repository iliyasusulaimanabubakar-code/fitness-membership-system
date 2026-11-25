
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
