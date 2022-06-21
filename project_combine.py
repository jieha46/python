"""----------Calculator----------"""
from ast import operator
from secrets import choice

# Addition operation
def addition ():
    print('{} + {} = '.format(num1, num2))
    print(num1+num2)
    print("***********************************")  

# Subtraction operation
def subtraction ():
    print('{} - {} = '.format(num1, num2))
    print(num1-num2)
    print("***********************************")

# Multiplication operation
def multiplication ():
    print('{} x {} = '.format(num1, num2))
    print(num1*num2)
    print("***********************************")

# Division operation
def division ():
    print('{} / {} = '.format(num1, num2))
    print(num1/num2)
    print("***********************************")

# Squares operation
def squares():
    print('{} ^2 = '.format(num1))
    print(num1*num1)
    print("***********************************")

# Square Root operation
def squareroot():
    print('sqrt  {} = '.format(num1))
    print(pow(num1, 0.5 ))
    print("***********************************")

# Cubes operation
def cubes():
    print('{} ^3 = '.format(num1))
    print(num1**num1)
    print("***********************************")

# Cube Root operation
def cuberoot():
    print('cbrt  {} = '.format(num1))
    print(num1**(1/3))
    print("***********************************")


#main...

while True:
    print("****************************************") 
    print("\n Simple Calculator & BMI Calculator\n ")
    print(" Choose your option:\n")
    print("  Enter 'A' Simple Calculator")
    print("  Enter 'B' BMI Calculator")
    print("  Enter 'Q' Quit")
    calc = input ("  Please enter your option here: " ' ')
    if calc == 'A': 
        # Simple Calculator operation
        list = []
        # User choose operation needed
        print(" Choose an operation\n")
        print("  Enter 'a' for Addition")
        print("  Enter 's' for Substraction")
        print("  Enter 'm' for Multiplication")
        print("  Enter 'd' for Division")
        print("  Enter 'sq' for Squares")
        print("  Enter 'sqrt' for Square root")
        print("  Enter 'cb' for Cubes")
        print("  Enter 'cbrt' for Cube root")
        print("  Enter 'q' for Quit")
        print("-----------------------------------\n")
        # User selection display
        c = input("Enter your selection:" ' ')
        if c != 'q':
            # Addition operation
            if c == 'a':
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                addition()
            # Subtraction operation
            elif c == 's': 
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                subtraction()
            # Multiplication operation
            elif c == 'm': 
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                multiplication()
            # Division operation
            elif c == 'd':
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                division()
            # Squares operation
            elif c == 'sq':
                num1=int(input("Enter the Number:"))
                squares()
            # Square Root operation
            elif c == 'sqrt':
                num1=int(input("Enter the Number:"))
                squareroot()
            # Cubes operation
            elif c == 'cb':
                num1=int(input("Enter the Number:"))
                cubes()
            # Cube Root operation
            elif c == 'cbrt':
                num1=int(input("Enter the Number:"))
                cuberoot()
            else:
                print ("Sorry, invilid character")
        else:
            break

    # BMI Calculator
    elif calc == 'B':
        """Print "Body Mass Index" and return None."""
        # User input on height and weight
        print ("******************************************************")
        print ("Calculator for Body Mass Index")
        nama = str(input("Your name : "))
        tinggi = float(input ("Please insert your height in metres: "))
        berat = float(input ("Please insert your weight in kilograms: "))
        bmi = (berat) / (tinggi**2)
        print ("******************************************************")
        print ("Your BMI is", round (bmi, 2))
        if  (bmi < 16):
            print ("You're underweight (moderate)")

        elif (bmi >= 16 and bmi < 18.5):
            print ("You're underweight (mild)")

        elif (bmi >= 18.5 and bmi < 25):
            print ("You're normal")

        elif (bmi >= 25 and bmi < 30):
            print ("You're overweight")

        elif (bmi >= 30):
            print ("You're obese")
    else:
        break
    
