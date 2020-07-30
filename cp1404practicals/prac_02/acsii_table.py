LOWER_LIMIT = 33
UPPER_LIMIT = 127



character = input("Enter a Character: ")
print("The ACSII code for {0} is {1}".format(character, ord(character)))

number = int(input("Enter a number between {0} and {1}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
while number < LOWER_LIMIT or number > UPPER_LIMIT:
    print("Invalid choice")
    number = int(input("Enter a number between {0} and {1}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
print("The character for {0} is {1}".format(number, chr(number)))

