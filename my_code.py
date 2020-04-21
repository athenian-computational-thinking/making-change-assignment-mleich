from py_extras import change_stmt


def make_change(cost, amount_given):
    # Enter you code here
    # Consider using variables that match the variables used in the call to change_stmt() below

    # This will be the final statement of make_change() and will return the appropriate string
    return change_stmt(twenties, tens, fives, ones, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
    # Test your code with this first 
    # Change the cost and paid values to try different inputs
    cost = 45.33
    paid = 77.22
    s = make_change(cost, paid)
    print(s)

    # After you are satisfied with your results, use input() calls to prompt the user for values:
    # cost = float(input("Cost of the items: "))
    # paid = float(input("Amount paid: "))
    # print(make_change(cost, paid))