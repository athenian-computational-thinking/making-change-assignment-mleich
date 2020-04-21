# change_stmt() accepts the number of bills/coins you want to return and
# creates the appropriate string
def change_stmt(twenties, tens, fives, ones, quarters, dimes, nickels, pennies):
    if twenties == 0 and tens == 0 and fives == 0 and ones == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        return "No change returned."

    prefix = "Your change will be:"
    s = prefix
    if twenties > 0:
        s += " {} $20".format(twenties)
    if tens > 0:
        if s != prefix:
            s += ","
        s += " {} $10".format(tens)
    if fives > 0:
        if s != prefix:
            s += ","
        s += " {} $5".format(fives)
    if ones > 0:
        if s != prefix:
            s += ","
        s += " {} $1".format(ones)
    if quarters > 0:
        if s != prefix:
            s += ","
        s += " {} $.25".format(quarters)
    if dimes > 0:
        if s != prefix:
            s += ","
        s += " {} $.10".format(dimes)
    if nickels > 0:
        if s != prefix:
            s += ","
        s += " {} $.05".format(nickels)
    if pennies > 0:
        if s != prefix:
            s += ","
        s += " {} $.01".format(pennies)
    return s
