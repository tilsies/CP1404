num_items = int(input("Enter number of items: "))
total_cost = 0
while num_items < 0:
    print("Invalid number of items")
    num_items = int(input("Enter number of items: "))

for i in range(1,num_items+1):
    item_price = float(input("Price of item: $"))
    total_cost += item_price

if total_cost > 100:
    total_cost *= 0.9

print("Total price for {0} items is ${1:.2f}".format(num_items,total_cost))


