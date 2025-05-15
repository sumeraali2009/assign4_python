"""
Program: add2numbers
--------------------
This program asks the user for two integers
and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Prompting for the first number
    num1 = int(input("Enter the first number: "))
    
    # Prompting for the second number
    num2 = int(input("Enter the second number: "))
    
    # Calculating the sum
    total = num1 + num2
    
    # Displaying the result
    print("The total is " + str(total) + ".")

# This line calls the main function when the script runs
if __name__ == '__main__':
    main()
