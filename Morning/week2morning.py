#Comparators
"""
check if 1 is greater than 2
check if 1 is equal to 2
check if 1 is greater than or equal to 2
check if 1 is not equal to 2
"""

1 > 2
1 == 2
1 >= 2
1 != 2

#Boolean Operators (and, or, not)
"""
check if 1 is less than 2 and 2 is less than 3 on one line
check if 1 is less than 2 or 2 is greater than 3 on one line
"""


1 < 2 or 2 > 3

#If, Elif, and Else statements
python = "snake"

"""
If 1 is greater than 2, print "foo". Else print "bar"

If python equals "snake", print "python is a snake". Else print "not a snake"

If 5*5 is equal to 30, print "5*5 is 30". Elif 5*5 is equal to 25, print
"5*5 is 25". Else print "5*5 is not 25 or 30"

If 1 is less than 2 and 2 is less than 3, print "True". Else print "False"

If 1 is less than 2 or 2 is greater than 3, print "True". Else print "False"

If 1 is less than 2, then if 1 is less than 3, print "Nested If statement". Else
print "False" for both if statements.

If i == True, print "True". Else print "False"
"""

if 1 > 2:
    print ("foo")
else:
    print ("bar")

python = "snake"
if python == "snake":
    print("python is a snake")
else:
    print("not a snake")

if 5*5 == 30:
    print ("5*5 is 30")
elif 5*5 == 25:
    print ("5*5 is 25")
else:
    print ("5*5 is not 25 or 30")

if 1 < 2 and 2 < 3:
    print("True")
else:
    print("False")

if 1 < 2 or 2 > 3:
    print("True")
else:
    print("False")

if 1 < 2:
    if 1 < 3:
        print("Nested if statement")
    else:
        print("False")
else:
    print("False")

i = True
if i:
    print("True")
else:
    print("False")
