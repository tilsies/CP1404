from guitar import Guitar

def main():

    guitars = []
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)

        guitars.append(new_guitar)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars: ")

        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage = "(Vintage)"
            else:
                vintage = ""

            print("Guitar {}: {:<20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage))

    else:
        print("No guitars?!")

if __name__ == '__main__':
    main()
