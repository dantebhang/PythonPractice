my_name = "Dante"
print("Welcome to the course, " + my_name + "!")

# this is a comment

'''This
is 
a multi
line
comment'''

# print is like console.log
print("Hello World")

# printing multi-lines

print("""Two roads diverged in a wood, and I—
I took the one less traveled by, 
And that has made all the difference.""")

print('"Hurray"')

name = "Dante"
print(name)

baseball_season = 2000
strikeouts = 100
earned_run_average = 2.5

print("hello" + " python")

message_start = "A marathon is"
message_finish = "miles."
marathon_distance = 26.2

# Print a string that says:
# "A marathon is 26.2 miles."
print(message_start, marathon_distance, message_finish)


# Take the initial income you earn per hour and multiply
# that by the hours you worked that day and print the results.

# Income earned per hour
income = 10

# Hours worked today
hours_worked_today = 5

# Find income earned today
income *= hours_worked_today  #income = income * hours_worked_today
# Print todays income
print(income)


# importing math to give us access to the floor() method
import math

# floating point value that we want to round down
dollars = 82.12

# assign to whole_dollar the value of dollars passed to the math.round() function
whole_dollar = math.floor(dollars)

print(whole_dollar)
# Prints 82



# import in the math library
import math

# This is the amount of money you have in your piggy bank
money_in_piggy_bank = 42.75

# Print the value of money in your piggy bank rounded to the nearest integer
rounded_money = math.ceil(money_in_piggy_bank) #round up
print(rounded_money)
print(math.floor(42.75)) #round down