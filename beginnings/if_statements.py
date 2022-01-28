def can_i_buy_a_dog(money):
    if money >= 300:
        print("Congratulations, you can buy a dog!")
# Add if statement to evaluate if money is greater than or equal to 300
# If it is print the message "Congratulations, you can buy a dog!"


# can_i_buy_a_dog(300)


name = "Jim"

# Use the `.upper()` function to make this statement true and
# print "Hello Jim, good to see you."
if name.upper() == "JIM":
    print("Hello Jim, good to see you.")


def how_to_dress(temperature):
    if temperature >= 75:
        print("Today is a good day for shorts.")
    else:
        print("Today is a good day for a jacket")


# Call the `how_to_dress()` function two times.
# The first time to print "Today is a good day for shorts."
# The secont time to print "Today is a good day for a jacket"
# how_to_dress(80)
# how_to_dress(70)

money_in_pocket = 3
money_in_banking_account = 3

if (money_in_pocket > 5) or (money_in_banking_account > 5):
    print("I would like to buy a cup of coffee.")
else:
    print("I think I will find a drinking fountain.")




temperature = 70
get_off_work_early = True

if (temperature < 80) and (get_off_work_early):
    print("I am going to go for a run.")
else:
    print("I don't think I will be able to go for a run today.")
