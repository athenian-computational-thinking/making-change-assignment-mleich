from py_extras import change_stmt


def make_change(cost, amount_given):
        
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # Making change in pennies (to avoid float math)
    change = round(((amount_given - cost) * 100), 2)
    print ("Your change is: "+ str(change) + " cents")

    #How many $20 bills?
    while change >= 2000:
        twenties += 1
        change -= 2000

    # How many $10 bills?
    while change >= 1000:
        tens += 1
        change -= 1000

    # fives
    while change >= 500:
        fives += 1
        change -= 500

    # ones
    while change >= 100:
        ones += 1
        change -= 100

    #Coins
    while change >= 25:
        quarters += 1
        change -= 25

    while change >= 10:
        dimes += 1
        change -= 10

    while change >= 5:
        nickels += 1
        change -= 5

    while change >= .5:
        pennies += 1
        change -= 1

    print (change)
    # This will be the final statement of make_change() and will return the appropriate string
    return change_stmt(twenties, tens, fives, ones, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
    # Test your code with this first 
    # Change the cost and paid values to try different inputs
    cost = 60
    paid = 117.24
    #cost = float(input("What is the total cost? "))
    #paid = float(input("How much did you pay? "))
    s = make_change(cost, paid)
    print(s)

    # After you are satisfied with your results, use input() calls to prompt the user for values:
    # cost = float(input("Cost of the items: "))
    # paid = float(input("Amount paid: "))
    # print(make_change(cost, paid))