"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When the numerator/denominator input is a string/float (e.g a / 1.5)
2. When will a ZeroDivisionError occur?
   When the denominator input == 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Add while loop for denominator == 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can not be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
