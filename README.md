# Making Change Assignment 

## Problem Description
Write a program that calculates the change in a purchase. 

* Prompt the user for the cost of the items and the amount paid. 
* Use the largest unit of currency you can before stepping down to the next level. 
* The largest bill that can be used for change is a $20 bill.
* You can assume that the amount paid will be >= cost of the items
* Use the provided `change_stmt()` function in [py_extras.py](./py_extras.py) to create the output string.

## Example
```
How much was the item? 12.50
How much was paid to the cashier? 20.00
The change will be: 1 $5.00, 2 $1, and 2 $.25.
```

## Suggested Approach
1) Calculate total change to return
1) Calculate the number of 20s to return 
1) After you calculate the number of 20s, recalculate the change to return
1) Repeat steps 2 and 3 for the other bills/coins
1) Use the provided `change_stmt()` function in [py_extras.py](./py_extras.py) to create the output string.
1) Print the output string returned from `change_stmt()`.


## Hints
* Use `input()` to prompt the user for a value. 
* Consider variable types. Will you be working with integers here?
* Use a python *repl*  to see what the value of `17.24 - 17.00` is. 
* You will see that some dollar amounts expressed with `float` cannot be properly represented. 
* The solution is to shift the amount by 2 decimal places and convert the amount to an `int`.
* Use a `print()` stmt to debug your intermediate values, e.g., `print("Change is " + str(change))`


Add code to [my_code.py](./my_code.py) to make it do the desired thing.

Run your code with: `python my_code.py`

Run your tests with: `pytest`