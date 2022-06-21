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
    if calc == 'A': # Simple Calculator operation
        list = []
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
        c = input(" ")
        if c != 'q':
            if c == 'a': # Addition operation
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                addition()

            elif c == 's': # Subtraction operation
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                subtraction()
            elif c == 'm': # Multiplication operation
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                multiplication()
            elif c == 'd': # Division operation
                num1=int(input("Enter 1st Number:"))
                num2=int(input("Enter 2nd Number:"))
                division()
            elif c == 'sq': # Squares operation
                num1=int(input("Enter the Number:"))
                squares()
            elif c == 'sqrt': # Square Root operation
                num1=int(input("Enter the Number:"))
                squareroot()
            elif c == 'cb': # Cubes operation
                num1=int(input("Enter the Number:"))
                cubes()
            elif c == 'cbrt': # Cube Root operation
                num1=int(input("Enter the Number:"))
                cuberoot()
            else:
                print ("Sorry, invilid character")
        else:
            break

    # BMI Calculator
    elif calc == 'B':
        """Print "Body Mass Index" and return None."""
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
    
