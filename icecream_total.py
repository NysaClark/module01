"""
    Nysa Clark
    Module 01 Programming Assignment
    Part A

    This program ...
"""

# Isaiah's Ice Cream 10% to customers from AZ "locals" discount
# and 15% to customers from Colorado "Broncos fan" discount
# and a $5 price increase for customers from Rhode Island
# cause a car w/ R.I. plates cut him off once 23 years ago

# prompt user for their state name
state_name = input("What state are you from? ");

# prompt user for the total of their ice cream purchase
total = int(input("What is the total amount of your ice cream purchase? "));

# create method that accepts both state name & purchase amount as params
# and returns the price after discount or extra charge
def calc_final_cost (state_name, total) :
    if state_name == "Arizona":
        explanation = "a 10% discount is given to customers from Arizona"
        return total - (total * .1), explanation
    elif state_name == "Colorado":
        explanation = "a 15% discount is given to customers from Colorado"
        return total - (total * .15), explanation
    elif state_name == "Rhode Island":
        explanation = "a $5 price increase is given to customers from Rhode Island because a car with R.I. plates cut Isaiah off once 23 years ago"
        return total + 5, explanation
    else:
        explanation = "you are not from AZ or CO"
        return total, explanation



[final_cost, explanation] = calc_final_cost(state_name, total)

# output a message w/ explanation of the customer's new total price
print(f"Your new total is ${final_cost} because {explanation}.")