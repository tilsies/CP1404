user_name = input("Enter your name: ")
print("(H)ello \n(G)oodbye \n(Q)uit")
choice = input(">").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {0}".format(user_name))
    elif choice == "G":
        print("Goodbye {0}".format(user_name))
    else:
        print("Invalid Choice! >=(")

    print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = input(">").upper()

if choice == "Q":
    print("Finished")
