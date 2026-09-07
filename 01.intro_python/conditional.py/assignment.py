

# A. Basic if 

num = int(input(" Enter number: "))
if num > 10:
    print("Greater than 10")

age = int(input(" Enter age: "))
if age >= 18:
    print("Adult")

num = int(input(" Enter number: "))
if num > 0:
    print("Positive")

marks = int(input(" Enter marks: "))
if marks >= 40:
    print("Pass")

num = int(input(" Enter number: "))
if num == 0:
    print("Zero")

#  B. if-else 

num = int(input(" Enter number: "))
print("Positive" if num > 0 else "Not positive")

age = int(input(" Enter age: "))
print("Adult" if age >= 18 else "Minor")

num = int(input(" Enter number: "))
print("Even" if num % 2 == 0 else "Odd")

marks = int(input(" Enter marks: "))
print("Pass" if marks >= 40 else "Fail")

a = int(input(" Enter first number: "))
b = int(input(" Enter second number: "))
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

# C. if-elif-else 

marks = int(input(" Enter marks: "))
if marks >= 90: print("A")
elif marks >= 75: print("B")
elif marks >= 60: print("C")
elif marks >= 40: print("D")
else: print("F")

num = int(input(" Enter number: "))
if num > 0: print("Positive")
elif num < 0: print("Negative")
else: print("Zero")

day = int(input(" Enter day number (1-5): "))
if day == 1: print("Monday")
elif day == 2: print("Tuesday")
elif day == 3: print("Wednesday")
elif day == 4: print("Thursday")
elif day == 5: print("Friday")
else: print("Other")

marks = int(input(" Enter marks: "))
if marks >= 90: print("Excellent")
elif marks >= 60: print("Good")
elif marks >= 40: print("Pass")
else: print("Fail")

num = int(input(" Enter number: "))
if num == 1: print("1")
elif num == 2: print("2")
elif num == 3: print("3")
else: print("Other")

# D. Nested Conditions
print("\n--- D. Nested ---")
age = int(input(" Enter age: "))
if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75: print("Good")
    else: print("Passed")
else:
    print("Failed")

num = int(input(" Enter number: "))
if num > 0:
    if num > 100:
        print("Positive and > 100")
    else:
        print("Positive but <= 100")

age = int(input(" Enter age: "))
if age >= 18:
    if age >= 60: print("Senior Adult")
    else: print("Adult")
else:
    print("Minor")

num = int(input(" Enter number: "))
if num != 0:
    if num > 0: print("Positive")
    else: print("Negative")
else:
    print("Zero is non-zero check failed")

# E. Multiple Conditions

age = int(input(" Enter age: "))
marks = int(input(" Enter marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")

num = int(input(" Enter number: "))
if num < 10 or num > 100:
    print("Special")

age = int(input(" Enter age: "))
has_id = input(" Has ID? True/False: ") == "True"
if age >= 18 and has_id:
    print("Allowed")

a = int(input(" Enter first: "))
b = int(input(" Enter second: "))
if a > 10 and b > 10:
    print("Both are greater than 10")

num = int(input(" Enter number: "))
if num < 0 or num > 100:
    print("Out of range ( <0 or >100 )")

# Logical Operators 

is_closed = False
if not is_closed:
    print("26. Open")

num = int(input(" Enter number: "))
if num >= 10 and num <= 50:
    print("Between 10 and 50")

num = int(input(" Enter number: "))
if num < 10 or num > 50:
    print("Outside 10 to 50")

is_student = True
has_id = True
has_ticket = True
if is_student and has_id and has_ticket:
    print(" Allowed")

age = int(input(" Enter age: "))
marks = int(input("30. Enter marks: "))
has_id = input("30. Has ID? True/False: ") == "True"
if age >= 18 and marks >= 40 and has_id:
    print("Eligible")
else:
    print("Not eligible")

# Explanation for 30: We use 'and' because ALL 3 conditions must be true together.
# 'or' would make it eligible even if only one is true, which is wrong.